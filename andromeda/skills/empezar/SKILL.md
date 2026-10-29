---
name: empezar
description: Úsalo el Día 1 de una instalación de Andromeda AI (AIS-OS), cuando alguien diga "configúrame", "empecemos", "llena mi AIOS", "set me up" u "onboard me", o si acaba de clonar el kit. Es un asistente todo en uno que hace el cuestionario de 7 preguntas Y al final genera los archivos del Día 1. Es idempotente, así que puedes volver a ejecutarlo cuando quieras después de editar aios-intake.md.
---

## Qué hace este skill

Es un solo asistente que:
- lee o escribe `aios-intake.md` (el cuestionario canónico);
- hace la entrevista de 7 preguntas si el archivo no está completo;
- al final genera en el mismo flujo los archivos del Día 1.

No existe un skill `/scaffold-from-intake` aparte: todo es un solo flujo.

Habla con el usuario en español latinoamericano neutro, salvo que prefiera otro idioma.

**El momento "wow":** al final, sugiere el prompt de cierre *"Prueba esto, pregúntame: ¿en qué debería enfocarme esta semana?"*. El usuario lo ejecuta una vez y ahí está el efecto. No hace falta guardar un skill `/hoy`: el prompt mismo siembra el marco de Mentalidad (el Default Shift) para que el usuario lo interiorice.

## Cuándo NO ejecutarlo

- Si el usuario ya hizo el onboarding y quiere actualizarlo: ejecútalo igual, pero salta las preguntas ya respondidas (es idempotente).
- Si el usuario quiere agregar una conexión nueva: eso no es onboarding. Indícale que edite `connections.md` directamente o que haga la Fase 2 de `/subir-nivel`.

## Ejecución

### Proyectos existentes e instalación portable

Lee primero el `AGENTS.md` y el `CLAUDE.md` que correspondan. Las rutas de abajo son las del kit base. En un proyecto ya establecido, usa sus fuentes canónicas equivalentes de contexto, voz y conexiones, en lugar de crear fuentes de verdad paralelas. Conserva las reglas operativas y el enrutamiento que no tengan relación, y sincroniza las ediciones del manual compartido cuando haga falta. El onboarding actualiza el contexto personal seleccionado, no todo el manual operativo.

Si falta `aios-intake.md`, usa la [plantilla del cuestionario](assets/aios-intake.md) incluida. Completa solo las respuestas que estén respaldadas explícitamente por fuentes existentes, con sus referencias, y deja lo desconocido para la entrevista. Instalar este skill no ejecuta el onboarding ni cambia el contexto del usuario.

### Paso 1: Lee el cuestionario

Lee `aios-intake.md`. Revisa qué secciones P1–P7 tienen contenido y cuáles siguen con los marcadores `[Tu respuesta aquí]`. En instalaciones anteriores pueden aparecer como Q1–Q7 y `[Your answer here]`: trátalos igual.

- **Todas completas:** salta el Paso 2 y ve al Paso 3 (generar archivos).
- **Algunas completas:** pregunta: "Veo que P1, P3 y P4 ya tienen respuesta. ¿Quieres completar el resto ahora o genero los archivos con lo que hay?". El usuario decide.
- **Ninguna completa (clon nuevo):** haz el Paso 2 como conversación.

### Paso 2: La entrevista (7 preguntas, límite estricto)

Haz una pregunta a la vez. Escribe cada respuesta en `aios-intake.md` sobre la marcha, para que el usuario pueda retomar si se interrumpe.

**P1 — ¿Quién eres, qué vendes y a quién se lo vendes?**
Identidad, oferta y cliente ideal (ICP). Basta con un párrafo para cada uno.

**P2 — Pega uno o dos textos que hayas escrito hace poco. No los edites.**
*Es la única pregunta con una regla estricta.* Las muestras de voz DEBEN pegarse, no escribirse en medio de la conversación. Si el usuario empieza a redactar un texto nuevo, recházalo:

> *"Espera: pégalo tal cual. Si lo escribes aquí mientras hablamos, la muestra ya queda moldeada por la conversación. Abre tu último correo o tu última publicación en otra pestaña y pega el texto sin editar. Esta es la única regla que no puedo flexibilizar."*

Pide dos muestras: un correo y una publicación, o dos de cualquiera de los dos.

**P3 — ¿Cuáles son tus 2 o 3 prioridades más importantes para los próximos 90 días?**
Prioridades del trimestre. Si dicen "hacer crecer mi negocio", insiste: que nombren una cifra, una fecha límite o un entregable.

**P4 — ¿Dónde entran realmente tus ingresos y dónde los registras?**
Puede haber varias respuestas. Corresponde al Dominio 1 del Nivel 1 (Ingresos/Finanzas).

**P5 — ¿Dónde hablas a diario con tus clientes, tu equipo y el resto del mundo?**
Correo (Gmail/Outlook), WhatsApp, Slack/Teams/Discord, DMs. Corresponde a los Dominios 2 y 4.

**P6 — ¿Dónde guardas las grabaciones de reuniones, las notas y los documentos importantes?**
Corresponde a los Dominios 6 y 7.

**P7 — ¿Cuál es la tarea que más tiempo te consume en la semana y dónde llevas hoy el control de tu trabajo?**
Registra `top_pain` (lo usa `/subir-nivel` el Día 14) y el Dominio 5 (tareas).

El Dominio 3 (Calendario) se deduce de P5: Gmail → Google Calendar; Outlook → calendario de Outlook. Confírmalo en el Paso 3.

### Paso 3: Genera los archivos del Día 1

Cuando el cuestionario esté completo, genera estos archivos (o actualízalos si es una nueva ejecución). Si ya existen, respalda los originales en `archives/intake-{YYYY-MM-DD-HHMM}/`.

1. **`context/about-me.md`**: a partir de P1 (identidad, rol) y P7 (`top_pain`). Un párrafo corto para cada tema.
2. **`context/about-business.md`**: a partir de P1 (oferta, cliente ideal) y P4 (modelo de ingresos). Un párrafo.
3. **`context/priorities.md`**: a partir de P3. Lista numerada, una línea por prioridad.
4. **`references/voice.md`**: a partir de P2. Pega las muestras textualmente, con un encabezado breve que explique su uso ("Imita este registro al redactar; no finjas mi voz en contenido externo sin mostrármelo primero").
5. **`connections.md`**: llena la tabla de 7 filas con las respuestas de P4 a P7. Cada fila lleva `mecanismo: aún no conectado`, `autenticación: —` y `última revisión: —`. El usuario configura las conexiones el Día 2.
6. **Manual operativo (`AGENTS.md` / `CLAUDE.md`)**: reemplaza los marcadores `{{...}}` que correspondan con el nombre del usuario, su prioridad, un resumen de su voz y un resumen de sus conexiones. En un manual ya establecido, actualiza solo el contexto seleccionado o su ruta, y conserva las demás instrucciones. Mantén sincronizada la guía compartida cuando el proyecto lo requiera.

Los nombres de archivos y carpetas (`context/about-me.md`, etc.) se mantienen en inglés por compatibilidad con los demás skills. El contenido va en el idioma del usuario.

### Paso 4: La pantalla de cierre

Muestra una sola pantalla, de tres líneas como máximo:

```
✓ Día 1 listo. Tu AIOS ya sabe quién eres, qué vendes, qué importa este trimestre y cómo suenas.

Hoy: pregúntame "¿en qué debería enfocarme esta semana?"
Mañana: elige una herramienta de connections.md y conéctala (instalación manual de un MCP o un script pequeño de API + guardar references/{herramienta}-api.md).
Día 7: ejecuta /auditar para ver tu puntaje.
```

Cuando el usuario use el prompt de cierre ("¿en qué debería enfocarme esta semana?"), responde usando solo los nuevos archivos de contexto. Incluye:
- una lista de 3 prioridades, en el registro de voz de P2;
- que cada punto se relacione con una prioridad de 90 días de P3;
- esta línea final: *"Si tuviera que elegir una sola cosa para el lunes, sería [X], porque [razón según tus prioridades]. ¿Quieres que redacte el primer correo? Y una pregunta: ¿dónde podrías aplicar aquí el Default Shift? ¿Hasta qué punto podría la IA encargarse de esta tarea?"*

La pregunta del Default Shift siembra el marco de Mentalidad antes de que `/subir-nivel` lo presente formalmente el Día 14.

## Reglas críticas de implementación

1. **El límite de 7 preguntas no se negocia.** No agregues una P8 en la conversación.
2. **No se puede saltar la muestra de voz pegada.** Si el usuario escribe muestras en el chat, recházalas y pídele que pegue textos reales.
3. **Generación en un solo paso.** Al terminar el Paso 2, escribe todos los archivos del Paso 3 de una vez, sin confirmaciones en varios turnos. El usuario itera editando `aios-intake.md` y volviendo a ejecutar el skill.
4. **Idempotente.** Volver a ejecutarlo con el cuestionario editado actualiza los archivos de contexto y respalda los originales en `archives/intake-{ts}/`. Salta las preguntas ya respondidas, salvo que el usuario quiera revisarlas.
5. **La pantalla de cierre tiene tres líneas.** No es un menú.
6. **No generes skills extra.** No crees `/hoy`, `/redactar`, `/conectar-herramienta`, etc. El kit trae seis skills: `/empezar`, `/auditar`, `/entrevistame`, `/conectar`, `/subir-nivel` y `/cerebro-3d`. El usuario crea los demás con `/subir-nivel`.
7. **`references/3ms-framework.md` es de solo lectura.** Ya viene en el kit. No lo sobrescribas.
8. **No escribas en `.env`.** No pidas claves de API el Día 1: las conexiones llegan el Día 2.

## Verificación (para quien implementa)

- **Prueba en frío:** clona un kit nuevo, ejecuta `/empezar`, responde las 7 preguntas, deja que genere los archivos y haz el prompt "wow". La respuesta debe citar específicamente P1, P3 y P7. Si es genérica, falla.
- **Idempotencia:** vuelve a ejecutar `/empezar` cambiando una prioridad de P3. Resultado esperado: solo se actualizan `context/priorities.md` y la sección de prioridades de `CLAUDE.md`, y se crea un respaldo en `archives/intake-{ts}/`.
- **Rechazo de voz:** escribe una muestra en el chat. Resultado esperado: el skill la rechaza y pide que la pegues.

> *Adaptado de The Three Ms of AI™ © 2026 Nate Herk. El lenguaje de Mentalidad de la pantalla de cierre viene de `references/3ms-framework.md`. Traducción al español: Andromeda AI.*
