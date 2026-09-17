# EXPANSIONES: qué agregar a medida que creces

El kit viene liviano a propósito: seis skills y un pequeño conjunto de archivos de contexto y referencia. A medida que crezcas, usa `/conectar` para agregar fuentes nuevas en la ruta correcta y `/auditar` para comprobar que la información siga siendo fácil de encontrar y esté al día.

La estructura del AIOS debe parecerse a un negocio pequeño y bien administrado, no a un sótano donde se acumula de todo.

Los nombres de carpetas (`context/`, `references/`, `projects/`, etc.) se mantienen en inglés porque los skills y el Cerebro 3D los reconocen así.

---

## Qué trae el kit (no lo quites)

| Carpeta / archivo | Propósito |
|---|---|
| `context/` | Sobre ti, tu negocio y tus prioridades. Lo llena `/empezar`. |
| `references/` | Frameworks, muestras de voz, guías de API y procedimientos a medida que los construyes. |
| `references/andromeda/` | Espacio reservado para los frameworks y el conocimiento propios de Andromeda AI. |
| `decisions/log.md` | Registro de solo anexar con lo que se decidió y por qué. |
| `brainstorms/` | Entrevistas guardadas de `/entrevistame`; se crea la primera vez que lo usas. El contexto confirmado enlaza a su captura. |
| `archives/` | Archivos viejos. No los borres: muévelos aquí. |
| `connections.md` | Registro de todos los sistemas a los que puede acceder tu AIOS. |
| `.claude/skills/` | Tus skills: `/empezar`, `/auditar`, `/subir-nivel`, `/conectar`, `/entrevistame` y `/cerebro-3d`. Agrega más solo si resuelven una necesidad real. |
| `aios-intake.md` | Fuente de verdad para `/empezar`. Edítalo y vuelve a ejecutarlo cuando quieras. |
| `CLAUDE.md` | Manual operativo raíz. Lo llena `/empezar`. Edítalo cuando cambien tu rol o tu voz. |

---

## Qué agregar a medida que creces

| Carpeta / archivo | Agrégalo cuando | Por qué |
|---|---|---|
| `projects/` | Tengas 2 o más frentes de trabajo continuos con su propio contexto | Los proyectos activos necesitan contexto propio, separado de los archivos permanentes de `context/` |
| `templates/` | Te sorprendas copiando y pegando los mismos prompts o estructuras de documentos | Puntos de partida reutilizables y parametrizados; evitan que las versiones se desvíen |
| `brand-assets/` | Generes contenido visual (carruseles, diapositivas, miniaturas, imágenes) | Centraliza logos, paletas, fuentes, voz y tono; el AIOS los consulta en vez de adivinar |
| `references/sops/` | Documentes cómo funcionan los procesos recurrentes | Procedimientos operativos estándar que el AIOS lee para ejecutar las cosas de forma consistente |
| `references/{herramienta}-api.md` | Conectes una API o un MCP nuevo y entiendas cómo funciona | Se investiga una vez y queda guardado para siempre. `/auditar` lo valora y los skills futuros no tienen que volver a investigar. |
| `scripts/` | Escribas Python o Bash para consultar APIs que ningún MCP cubre | Para la mayoría, la segunda conexión es un script, no un MCP |
| `.claude/agents/` | Necesites un subasistente para investigación o redacción repetible de varios pasos | Los agentes corren en modelos más económicos y con su propio contexto, así tu sesión principal queda liviana |
| Carpetas de sub-OS (por ejemplo, `youtube-os/`) | Tengas una vertical con sus propios datos, hojas, transcripciones y scripts | Patrón de aislamiento: cada vertical tiene su propio manual operativo y sus skills |

---

## Frecuencias sugeridas

Cada cuánto conviene revisar cada parte:

- `decisions/log.md`: con cada decisión importante (la Fase 2 de `/subir-nivel` las registra automáticamente).
- `archives/`: limpieza trimestral; mueve proyectos inactivos, skills en desuso y versiones viejas del cuestionario.
- `references/sops/`: cuando alguien nuevo vuelva a ejecutar un proceso, escribe el procedimiento.
- `connections.md`: cada vez que conectes una herramienta nueva, agrega una fila.
- `references/{herramienta}-api.md`: al mismo tiempo que actualizas `connections.md`; documenta la API una sola vez.
- `CLAUDE.md`: revisión trimestral; reescribe la sección de perfil y prioridades después de la revisión de 90 días de `/subir-nivel`.

---

## Qué NO agregar

Antipatrones. Parecen útiles, pero deterioran la estructura:

- **No vuelques archivos completos de correo o Slack en `references/`.** La wiki no es un depósito de documentos: solo hechos interpretados.
- **No armes carpetas dentro de carpetas para aparentar orden.** Una estructura plana con buenos nombres le gana a un anidamiento profundo. Si necesitas una jerarquía de carpetas para encontrar algo, tienes un problema de búsqueda, no de organización.
- **No agregues `notes/`, `misc/`, `tmp/` ni `inbox/`.** Terminan siendo cementerios. Si algo es viejo, usa `archives/`; si es nuevo, escribe un archivo real en el lugar correcto.
- **No crees de antemano carpetas que todavía no necesitas.** Las carpetas vacías son ruido. El AIOS te dirá cuándo es el momento.
- **No tengas `decisions.md` y `decisions/log.md` al mismo tiempo.** Elige uno. El kit trae `decisions/log.md`.
- **No dupliques tu manual operativo.** Hay un solo `CLAUDE.md` en la raíz. Las carpetas de sub-OS pueden tener su propio CLAUDE.md con alcance limitado, pero el de la raíz es el canónico.

---

## Cómo saber cuándo agregar una carpeta

Hazte tres preguntas:

1. **¿Es algo conceptualmente nuevo?** ¿O cabe en algo que ya existe?
2. **¿Lo voy a usar 3 o más veces en el próximo mes?** Si no, es prematuro.
3. **¿Podría `/subir-nivel` dirigir naturalmente un skill futuro hacia aquí?** Si sí, el AIOS lo va a usar. Si no, estás organizando para ti, no para el sistema.

Dos respuestas afirmativas: agrégala. Una sola: espera.

---

> *La estructura de tu AIOS debe parecerse a un negocio pequeño y bien administrado, no a un sótano donde se acumula de todo. Si no encuentras algo, es señal de consolidar, no de agregar otra carpeta.*
