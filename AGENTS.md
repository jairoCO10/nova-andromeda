# NOVA · Guía del asistente local

NOVA es un asistente personal que se ejecuta localmente con Ollama. El perfil, los recuerdos de SQLite y los planes se leen por los módulos existentes de `app.py`. Los flujos Andromeda se ejecutan en `andromeda_runtime.py`; sus instrucciones y recursos se conservan en `andromeda/skills/` y en las copias compatibles de `.agents/skills/` y `.claude/skills/` cuando estén disponibles.

## Fuentes y privacidad

- `perfil/`: contexto personal configurado. No lo publiques ni lo trates como vigente sin confirmación reciente.
- `data/nova.sqlite3`: recuerdos y planes locales. Nunca muestres la base completa ni la subas a Git.
- `context/`: respuestas privadas de `/empezar`.
- `brainstorms/`: entrevistas guardadas por `/entrevistame` y `/subir-nivel`.
- `connections.md`: índice local de rutas y fuentes; registrar una ruta no significa leer su contenido.
- `audits/` y `decisions/log.md`: archivos locales potencialmente privados.
- El Cerebro 3D usa solo fuentes seleccionadas explícitamente. No incluyas perfiles, bases de datos o secretos por defecto.

Los archivos privados y generados están cubiertos por `.gitignore`. Revisa `git status --ignored` y los cambios antes de publicar.

## Comandos

- `/empezar`: entrevista inicial de siete preguntas, guardada por respuesta, que prepara archivos en `context/`.
- `/entrevistame [tema]`: entrevista adaptativa de una pregunta por turno; captura y resumen local en `brainstorms/`.
- `/conectar <ruta> <propósito>`: valida y registra una fuente, sin copiar ni leer su contenido.
- `/auditar`: revisa rutas y estructura de las Cuatro C; guarda un reporte local fechado.
- `/subir-nivel`: entrevista de las 3 M y propone una mejora acotada sin ejecutar cambios por sí sola.
- `/cerebro-3d`: pregunta el nombre y las categorías, crea el globo 3D de Andromeda y lo sirve solo en `127.0.0.1`.

Los comandos de memoria de NOVA permanecen disponibles en `/ayuda`. Los recuerdos explícitos y los planes se conservan en SQLite con las reglas actuales del proyecto.

## Reglas de implementación

- Mantén `app.py` y el módulo Andromeda compatibles con Python 3.10 o superior.
- Ollama es el único proveedor de inferencia del asistente; usa `NOVA_MODEL` para seleccionar el modelo.
- Las entrevistas guardan cada respuesta antes de pasar a la siguiente pregunta. Las ideas tentativas se marcan como tales; nunca se convierten en hechos confirmados.
- `/conectar` solo registra rutas; el escaneo de fuentes ocurre únicamente al construir el cerebro 3D y después de elegirlas.
- El servidor del cerebro escucha en loopback. No expongas el puerto a la red ni detengas procesos ajenos.
- Conserva `LICENSE`, `NOTICE.md` y los avisos de dependencias. No atribuyas a NOVA la autoría del renderer 3D original ni de los frameworks de Nate Herk o Andromeda AI.
- Sincroniza esta guía con `CLAUDE.md` cuando cambien las reglas compartidas.

## Procedencia

Este fork adapta [Andromeda AI](https://github.com/Miguel21313/andromeda-ai), derivado de [AIS-OS](https://github.com/nateherkai/AIS-OS). Revisa `NOTICE.md` antes de cambiar atribuciones o redistribuir recursos.
