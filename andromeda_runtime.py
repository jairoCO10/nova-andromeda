"""Local Andromeda workflows for the NOVA + Ollama console."""

from __future__ import annotations

import json
import re
import shlex
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import webbrowser
from datetime import datetime
from pathlib import Path


ONBOARDING_QUESTIONS = (
    ("Uso", "¿Para qué quieres usar NOVA principalmente: vida personal, trabajo, estudio o una mezcla?"),
    ("Prioridades", "¿Cuáles son tus 2 o 3 prioridades para los próximos 90 días?"),
    ("Preferencias", "¿Cómo prefieres que NOVA te responda o te ayude? Da ejemplos si quieres."),
    ("Proyectos", "¿Qué proyectos o responsabilidades quieres que NOVA tenga presentes?"),
    ("Fuentes", "¿En qué archivos o sistemas guardas la información que consultas con frecuencia? No compartas claves ni contraseñas."),
    ("Trabajo repetido", "¿Qué tarea repites cada semana y te gustaría hacer con menos esfuerzo?"),
    ("Límites", "¿Qué información o acciones prefieres que NOVA no guarde ni haga sin preguntarte?"),
)

LEVEL_UP_QUESTIONS = (
    ("Frecuencia", "¿Qué tarea hiciste varias veces esta semana?"),
    ("Esfuerzo", "¿Qué parte fue manual, repetitiva o de copiar y pegar?"),
    ("Restricción", "¿Qué problema o cuello de botella resolvería mejorar esa tarea?"),
    ("Proceso", "¿Qué la inicia, qué información usa y cuál sería el resultado final?"),
    ("Autonomía", "¿Qué nivel prefieres: sugerencia, borrador para revisar o ejecución supervisada?"),
    ("Medida", "¿Cómo sabrías que mejoró: tiempo, errores, costo u otra medida concreta?"),
)


def _today():
    return datetime.now().astimezone()


def _slug(value):
    value = value.casefold().strip()
    value = re.sub(r"[^a-z0-9áéíóúñ]+", "-", value)
    value = value.strip("-")[:48]
    return value or "sesion"


def _append(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def _new_capture(folder: Path, topic: str, prefix=""):
    folder.mkdir(parents=True, exist_ok=True)
    stamp = _today()
    base = f"{prefix}{stamp:%Y-%m-%d}-{_slug(topic)}"
    for suffix in range(1000):
        name = f"{base}{'-' + str(suffix) if suffix else ''}.md"
        path = folder / name
        try:
            with path.open("x", encoding="utf-8") as handle:
                handle.write(f"# {topic}\n\nFecha: {stamp.isoformat(timespec='minutes')}\n\n## Captura\n")
            return path
        except FileExistsError:
            continue
    raise OSError("No pude crear un nombre único para la sesión.")


def _model(ask, system, messages, temperature=0.5):
    prompt = [{"role": "system", "content": system}, *messages]
    return ask(prompt, temperature=temperature).strip()


def _run_interview(root, topic, questions, read, write, ask, capture=None, final_system=None):
    capture = capture or _new_capture(root / "brainstorms", topic)
    write(f"NOVA: Guardaré esta sesión localmente en {capture.relative_to(root)}. Escribe /terminar para cerrar o /cancelar para detenerla.")
    transcript = []
    for index, (label, question) in enumerate(questions, 1):
        write(f"NOVA: {question}")
        answer = read("Jairo > ").strip()
        if answer.casefold() in {"/cancelar", "/salir"}:
            _append(capture, "\n\n> Sesión detenida por el usuario.\n")
            write(f"NOVA: Dejé la captura parcial en {capture.relative_to(root)}.")
            return capture
        if answer.casefold() == "/terminar":
            _append(capture, "\n\n> Sesión cerrada antes de completar todas las preguntas.\n")
            write(f"NOVA: Dejé la captura parcial en {capture.relative_to(root)}.")
            return capture
        transcript.extend(({"role": "assistant", "content": question}, {"role": "user", "content": answer}))
        _append(capture, f"\n### {index}. {label}\n\n{answer or '_Sin respuesta_'}\n")
    write("NOVA: Gracias. Estoy ordenando lo que conversamos.")
    summary = _model(
        ask,
        final_system or "Resume la entrevista en español claro. Separa hechos, ideas tentativas y preguntas pendientes. No inventes información ni declares que actualizaste otras fuentes.",
        transcript,
        temperature=0.2,
    )
    _append(capture, f"\n## Resumen\n\n{summary}\n")
    write(f"NOVA: La sesión quedó guardada en {capture.relative_to(root)}.\n\n{summary}")
    return capture


def _run_open_interview(root, topic, read, write, ask, capture):
    write(f"NOVA: Guardaré esta sesión localmente en {capture.relative_to(root)}. Responde con lo que sepas; escribe /terminar para cerrar o /cancelar para detenerla.")
    system = (
        "Eres NOVA y conduces una entrevista de descubrimiento en español. Haz una sola pregunta breve por turno, "
        "sin enumerar preguntas, sin responder por el usuario y sin inferir hechos. Basa cada pregunta en lo dicho "
        "y evita repetir información. Cuando ya haya contexto suficiente, responde únicamente LISTO."
    )
    question = f"¿Qué te gustaría entender, decidir o planear sobre {topic}?"
    transcript = []
    for index in range(1, 9):
        write(f"NOVA: {question}")
        answer = read("Jairo > ").strip()
        if answer.casefold() in {"/cancelar", "/salir"}:
            _append(capture, "\n\n> Sesión detenida por el usuario.\n")
            write(f"NOVA: Dejé la captura parcial en {capture.relative_to(root)}.")
            return
        if answer.casefold() == "/terminar":
            break
        _append(capture, f"\n### Intercambio {index}\n\n**NOVA:** {question}\n\n**Jairo:** {answer or '_Sin respuesta_'}\n")
        transcript.extend(({"role": "assistant", "content": question}, {"role": "user", "content": answer}))
        if ask is None or index == 8:
            break
        question = _model(ask, system, transcript, temperature=0.4)
        if not question or question.strip().upper() == "LISTO":
            break
    if ask is None:
        summary = "La entrevista quedó guardada; no hay conexión a Ollama para resumirla."
    else:
        summary = _model(
            ask,
            "Resume esta entrevista en español. Separa datos explícitos, hipótesis y pendientes. No inventes ni conviertas ideas tentativas en recuerdos confirmados.",
            transcript,
            temperature=0.2,
        )
    _append(capture, f"\n## Resumen\n\n{summary}\n")
    write(f"NOVA: La sesión quedó guardada en {capture.relative_to(root)}.\n\n{summary}")


def onboarding(root, read, write):
    intake = root / "aios-intake.md"
    content = intake.read_text(encoding="utf-8") if intake.exists() else ""
    existing = {
        int(number): answer.strip()
        for number, answer in re.findall(r"^## P(\d+)[^\n]*\n\n(.*?)(?=\n## P\d+|\Z)", content, re.M | re.S)
        if answer.strip() and answer.strip() != "_Pendiente_"
    }
    if not existing:
        intake.write_text("# Configuración local de NOVA\n\nRespuestas privadas; este archivo no se publica.\n", encoding="utf-8")
    answers = [None] * len(ONBOARDING_QUESTIONS)
    for index, (label, _) in enumerate(ONBOARDING_QUESTIONS, 1):
        if index in existing:
            answers[index - 1] = (label, existing[index])
    if all(answers):
        write("NOVA: La entrevista ya está completa. Regeneraré las páginas de contexto con las respuestas guardadas.")
    else:
        write("NOVA: Haré siete preguntas, una a la vez. Puedes escribir /cancelar para guardar el avance y retomarlo luego.")
    for index, (label, question) in enumerate(ONBOARDING_QUESTIONS, 1):
        if answers[index - 1] is not None:
            continue
        write(f"NOVA: {question}")
        answer = read("Jairo > ").strip()
        if answer.casefold() in {"/cancelar", "/salir"}:
            write(f"NOVA: Guardé el avance en {intake.relative_to(root)}. Ejecuta /empezar cuando quieras continuar.")
            return
        answers[index - 1] = (label, answer)
        _append(intake, f"\n## P{index} · {label}\n\n{answer or '_Pendiente_'}\n")
    sections = {
        "about-me.md": "Uso",
        "priorities.md": "Prioridades",
        "preferences.md": "Preferencias",
        "projects.md": "Proyectos",
        "sources.md": "Fuentes",
        "weekly-work.md": "Trabajo repetido",
        "boundaries.md": "Límites",
    }
    context = root / "context"
    context.mkdir(parents=True, exist_ok=True)
    archive_dir = root / "archives" / f"context-{_today():%Y%m%d-%H%M%S}"
    archived = False
    for filename in sections:
        previous = context / filename
        if previous.exists():
            archive_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(previous, archive_dir / filename)
            archived = True
    for (filename, label), (_, answer) in zip(sections.items(), answers):
        (context / filename).write_text(f"# {label}\n\n{answer}\n", encoding="utf-8")
    archived_note = f" Conservé las páginas anteriores en {archive_dir.relative_to(root)}." if archived else ""
    write("NOVA: Configuración completa. Dejé las respuestas en context/ para que NOVA pueda consultarlas en próximas sesiones. La captura original está en aios-intake.md." + archived_note)


def connect_source(root, argument, write):
    try:
        pieces = shlex.split(argument)
    except ValueError:
        pieces = []
    if len(pieces) < 2:
        write("NOVA: Usa /conectar ruta/al/archivo para qué sirve. Registro la ruta y su propósito; no copio ni leo el contenido.")
        return
    raw_path, purpose = pieces[0], " ".join(pieces[1:])
    source = Path(raw_path).expanduser()
    if not source.is_absolute():
        source = root / source
    try:
        resolved = source.resolve(strict=True)
    except OSError:
        write("NOVA: No encontré esa ruta. Revisa el nombre y vuelve a intentarlo.")
        return
    if resolved.is_file() and resolved.stat().st_size > 0:
        kind = "archivo"
    elif resolved.is_dir():
        kind = "carpeta"
    else:
        write("NOVA: La ruta no apunta a un archivo o carpeta disponible.")
        return
    shown = str(resolved.relative_to(root)) if resolved.is_relative_to(root) else str(resolved)
    record = root / "connections.md"
    if not record.exists():
        record.write_text("# Fuentes locales conectadas\n\nNOVA registra rutas para encontrarlas; no copia su contenido.\n", encoding="utf-8")
    _append(record, f"\n- **{shown}** ({kind}): {purpose.strip()}\n")
    write(f"NOVA: Registré {shown} como fuente. No leí ni copié el contenido ahora; NOVA podrá buscar fragmentos relevantes cuando hagas una consulta.")


def audit(root, write):
    checks = []
    for label, rel in (("Contexto", "context"), ("Referencias", "references"), ("Skills Andromeda", "andromeda/skills"), ("Conexiones", "connections.md"), ("Memoria local", "data/nova.sqlite3")):
        path = root / rel
        if path.is_dir():
            count = sum(1 for _ in path.rglob("*.md"))
            checks.append((label, f"disponible ({count} archivos Markdown)"))
        else:
            checks.append((label, "disponible" if path.is_file() else "sin configurar"))
    report = [f"# Auditoría NOVA — {_today():%Y-%m-%d %H:%M}", "", "Revisión local basada en rutas y archivos; no inspecciona el contenido privado de SQLite.", "", "## Contexto y capacidades"]
    report.extend(f"- **{label}:** {state}." for label, state in checks)
    report.extend(("", "## Conexiones y cadencia", "- Las rutas registradas en connections.md requieren verificación manual antes de considerarlas accesibles.", "- No se detectaron ejecuciones programadas; la cadencia depende del uso de NOVA.", "", "## Límites", "- Esta auditoría no valida la disponibilidad de Ollama, la vigencia del perfil ni el contenido de los planes."))
    destination = root / "audits" / f"audit-{_today():%Y-%m-%d-%H%M%S}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(report) + "\n", encoding="utf-8")
    write("NOVA: Auditoría guardada en " + str(destination.relative_to(root)) + "\n\n" + "\n".join(report[4:]))


def level_up(root, read, write, ask):
    path = _new_capture(root / "brainstorms", "subir-nivel", prefix="")
    _run_interview(
        root,
        "Subir nivel: 3 M",
        LEVEL_UP_QUESTIONS,
        read,
        write,
        ask,
        capture=path,
        final_system=(
            "A partir solo de las respuestas, redacta una propuesta breve de mejora usando Mentalidad, Método y Máquina: "
            "problema y evidencia, qué eliminar/automatizar/delegar, mapa del proceso, autonomía elegida, medida de éxito, "
            "primer entregable y preguntas pendientes. No escribas código ni ejecutes acciones. Marca como hipótesis lo que no esté confirmado."
        ),
    )


def _brain_sources(root, read, write):
    options = [
        ("README y guía de NOVA", "README.md"),
        ("Referencias y frameworks", "references"),
        ("Skills Andromeda", "andromeda/skills"),
        ("Proyectos", "projects"),
        ("Reuniones", "meetings"),
        ("Wiki", "wiki"),
        ("Contexto personal (puede contener datos privados)", "context"),
        ("Registro de decisiones (puede contener datos privados)", "decisions"),
    ]
    available = [(label, rel) for label, rel in options if (root / rel).is_dir()]
    if (root / "README.md").is_file():
        available.insert(0, ("README y guía de NOVA", "README.md"))
    available = list(dict.fromkeys(available))
    custom_index = len(available) + 1
    write("NOVA: El cerebro solo indexa Markdown y texto de las rutas aprobadas. Perfil, SQLite y copias no se preseleccionan; si eliges una carpeta que los contenga, sus notas de texto pueden entrar al grafo.")
    for index, (label, rel) in enumerate(available, 1):
        suffix = "" if (root / rel).is_file() else "/"
        write(f"  {index}. {label} — {rel}{suffix}")
    write(f"  {custom_index}. Otra ruta local de Markdown o texto")
    selected = read("Elige números separados por coma (ej. 1,2): ").strip()
    indices = set()
    for value in re.split(r"[,\s]+", selected):
        if value.isdigit() and 1 <= int(value) <= custom_index:
            indices.add(int(value))
    sources = [(available[i - 1][0], available[i - 1][1]) for i in sorted(indices) if i <= len(available)]
    if custom_index in indices:
        custom_path = read("Escribe la ruta exacta (no se copiará; solo se leerán archivos .md y .txt): ").strip().strip('"').strip("'")
        candidate = Path(custom_path).expanduser()
        if not candidate.is_absolute():
            candidate = root / candidate
        try:
            candidate = candidate.resolve(strict=True)
            if candidate.is_file() and candidate.suffix.casefold() not in {".md", ".txt"}:
                raise ValueError("Solo se admiten archivos Markdown o texto.")
            if not candidate.is_file() and not candidate.is_dir():
                raise ValueError("La ruta no apunta a un archivo o carpeta.")
        except (OSError, ValueError) as error:
            write(f"NOVA: No agregué esa ruta: {error}")
        else:
            label = read("Nombre para esta categoría: ").strip() or candidate.stem.replace("-", " ").replace("_", " ").title()
            path_value = candidate.relative_to(root).as_posix() if candidate.is_relative_to(root) else str(candidate)
            sources.append((label, path_value))
    return sources


def _brain_is_running(port, expected_name):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/graph", timeout=0.5) as response:
            graph = json.loads(response.read(8_000_000).decode("utf-8"))
        return graph.get("brain", {}).get("name") == expected_name
    except (OSError, ValueError, urllib.error.URLError):
        return False


def start_brain(root, read, write):
    node = shutil.which("node")
    if not node:
        write("NOVA: No encontré Node.js. Instala Node.js 22 o superior para usar el Cerebro 3D.")
        return
    version = subprocess.run([node, "--version"], capture_output=True, text=True, check=False).stdout.strip()
    match = re.search(r"v?(\d+)", version)
    if not match or int(match.group(1)) < 22:
        write(f"NOVA: El Cerebro 3D requiere Node.js 22 o superior. Versión disponible: {version or 'desconocida'}.")
        return
    app = root / "apps" / "3d-brain"
    config_path = app / "brain.config.json"
    if app.exists() and not config_path.is_file():
        write("NOVA: apps/3d-brain ya existe y no tiene brain.config.json. Para proteger sus archivos, no la sobrescribí.")
        return
    skill = root / "andromeda" / "skills" / "cerebro-3d"
    if not app.exists():
        name = read("¿Qué nombre quieres mostrar? (por defecto: Segundo Cerebro de NOVA): ").strip() or "Segundo Cerebro de NOVA"
        sources = _brain_sources(root, read, write)
        if not sources:
            write("NOVA: No elegiste fuentes. No creé una app con contenido inventado.")
            return
        config = {"name": name, "port": 4640, "sources": []}
        for index, (label, rel) in enumerate(sources):
            source_id = re.sub(r"[^a-z0-9-]", "", _slug(label).replace(" ", "-"))[:40] or f"fuente-{index + 1}"
            config["sources"].append({"id": source_id, "label": label, "paths": [rel]})
        config["sources"] = _unique_source_ids(config["sources"])
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
            json.dump(config, handle, ensure_ascii=False, indent=2)
            config_file = Path(handle.name)
        try:
            subprocess.run([node, str(skill / "scripts" / "scaffold.mjs"), "--root", str(root), "--config", str(config_file), "--out", "apps/3d-brain"], check=True, capture_output=True, text=True)
        except (subprocess.CalledProcessError, OSError) as error:
            detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
            write(f"NOVA: No pude preparar el Cerebro 3D: {detail}")
            return
        finally:
            config_file.unlink(missing_ok=True)
    try:
        subprocess.run([node, "build.mjs"], cwd=app, check=True, capture_output=True, text=True)
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", "") or str(error)
        write(f"NOVA: No pude construir el grafo: {detail.strip()}")
        return
    port = int(config.get("port", 4640))
    if _brain_is_running(port, config.get("name", "")):
        url = f"http://127.0.0.1:{port}"
        write(f"NOVA: El cerebro ya está activo en {url}.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        return
    with socket.socket() as sock:
        occupied = sock.connect_ex(("127.0.0.1", port)) == 0
    if occupied:
        for candidate in range(port + 1, min(port + 21, 65536)):
            with socket.socket() as sock:
                if sock.connect_ex(("127.0.0.1", candidate)) != 0:
                    port = candidate
                    config["port"] = port
                    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    break
        else:
            write("NOVA: No encontré un puerto libre cerca del puerto configurado. No detuve ningún servicio.")
            return
    try:
        with (app / "server.log").open("ab") as log:
            subprocess.Popen([node, "serve.mjs"], cwd=app, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    except OSError as error:
        write(f"NOVA: No pude iniciar el servidor local: {error}")
        return
    url = f"http://127.0.0.1:{port}"
    ready = False
    for _ in range(20):
        if _brain_is_running(port, config.get("name", "")):
            ready = True
            break
        time.sleep(0.15)
    if not ready:
        write(f"NOVA: El servidor no respondió en {url}. Revisa {app.relative_to(root)}/server.log.")
        return
    write(f"NOVA: {config.get('name', 'Cerebro 3D')} está listo en {url}.\nApp: {app.relative_to(root)}\nGrafo: apps/3d-brain/data/graph.json (local, ignorado por Git).\nArrastra para girar, desplázate para acercar; D reproduce la demo y C activa el modo cine.")
    try:
        webbrowser.open(url)
    except Exception:
        pass


def _unique_source_ids(sources):
    used = set()
    for index, source in enumerate(sources, 1):
        base = source["id"] or f"fuente-{index}"
        candidate = base
        suffix = 2
        while candidate in used:
            candidate = f"{base[:35]}-{suffix}"
            suffix += 1
        source["id"] = candidate
        used.add(candidate)
    return sources


def help_text():
    return (
        "Andromeda para NOVA: /empezar, /entrevistame [tema], /conectar <ruta> <propósito>, "
        "/auditar, /subir-nivel, /cerebro-3d. Las entrevistas y reportes se guardan localmente. "
        "También acepta frases directas como «entrevístame sobre mi viaje» o «construye mi cerebro 3D». "
        "El Cerebro 3D requiere Node.js 22 y solo lee las rutas que eliges."
    )


def detect_natural_command(text):
    """Recognize only explicit phrases so ordinary memories are not intercepted."""
    value = text.strip()
    patterns = (
        (r"^(?:nova[, ]+)?(?:empecemos|configura(?:r|me)?(?:\s+a\s+nova)?|quiero configurar nova)\b", "/empezar"),
        (r"^(?:nova[, ]+)?(?:entrev[ií]stame|hazme preguntas sobre|ay[uú]dame a explorar|quiero explorar)\b", "/entrevistame"),
        (r"^(?:nova[, ]+)?(?:audita(?:r)?(?:\s+a\s+nova)?|ejecuta una auditor[ií]a)\b", "/auditar"),
        (r"^(?:nova[, ]+)?(?:subamos de nivel|subir de nivel|mejoremos un flujo|hagamos una sesi[oó]n de las 3 m)\b", "/subir-nivel"),
        (r"^(?:nova[, ]+)?(?:construye|abre|inicia|crea) (?:(?:mi|un) )?(?:cerebro 3d|segundo cerebro)\b", "/cerebro-3d"),
        (r"^(?:nova[, ]+)?(?:conecta|registra)\s+", "/conectar"),
    )
    for pattern, command in patterns:
        match = re.match(pattern, value, re.I)
        if match:
            argument = value[match.end():].strip()
            if command == "/entrevistame":
                argument = re.sub(r"^(?:sobre|acerca de)\s+", "", argument, flags=re.I)
            return command, argument
    return None


def run_command(command, argument, *, root, read=input, write=print, ask=None):
    root = Path(root).resolve()
    if command == "/empezar":
        onboarding(root, read, write)
    elif command in {"/entrevistame", "/entrevístame"}:
        topic = argument.strip() or read("¿Qué tema quieres explorar? ").strip()
        if topic:
            capture = _new_capture(root / "brainstorms", topic)
            _run_open_interview(root, topic, read, write, ask, capture)
    elif command == "/conectar":
        connect_source(root, argument, write)
    elif command == "/auditar":
        audit(root, write)
    elif command == "/subir-nivel":
        if ask is None:
            write("NOVA: No hay un adaptador de Ollama disponible para preparar la propuesta.")
        else:
            level_up(root, read, write, ask)
    elif command == "/cerebro-3d":
        start_brain(root, read, write)
    else:
        write("NOVA: No reconozco ese comando de Andromeda.")
