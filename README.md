# Andromeda AI: tu Sistema Operativo de IA en español

**Andromeda AI** es una adaptación en español latinoamericano de [AIS-OS](https://github.com/nateherkai/AIS-OS), el kit de inicio de Nate Herk para convertir Claude Code o Codex en tu **Sistema Operativo de IA (AIOS)** personal. Esta adaptación la hizo Miguel Silva para creadores, emprendedores y usuarios de IA de Latinoamérica.

> **Procedencia:** el software y los frameworks originales son de **Nate Herk** (licencia MIT, © 2026 Nate Herk). Andromeda AI traduce y personaliza la experiencia; no reemplaza esa autoría. Los detalles están en [NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).

El kit se personaliza contigo mediante una entrevista inicial (`/empezar`).
- **`/entrevistame`:** para que entienda mejor tu negocio, tus preferencias o tus planes.
- **`/conectar`:** para que la información nueva se pueda encontrar.
- **`/auditar`:** para verificar el sistema.
- **`/subir-nivel`:** para cerrar una brecha útil a la vez.
- **`/cerebro-3d`:** para explorar tu conocimiento guardado como un globo interactivo: tu **Segundo Cerebro** en 3D.

> **AIS-OS** significa **AI Automation Society OS**: la forma en que Nate diseñó este AIOS para los miembros de su comunidad, [AI Automation Society](https://www.skool.com/ai-automation-society). El kit es universal y la estructura refleja cómo esos miembros gestionan sus negocios sobre él.

---

## Requisitos

- **[Claude Code](https://claude.com/claude-code)** (terminal, app de escritorio o extensión de IDE) **o Codex** (CLI o extensión de IDE).
- **Git**, para clonar el repositorio.
- **Node.js 22 o superior**, solo para el Cerebro 3D. El resto del kit es Markdown y no necesita instalar nada.
- **Opcional:** Bash (Git Bash en Windows) y Perl, si editas skills y quieres regenerar la copia de Codex con `scripts/sync-codex-skills.sh`.

## Instalación

```bash
git clone <URL-de-tu-copia-de-andromeda-ai> mi-aios
```

```bash
cd mi-aios
```

Abre la carpeta en Claude Code (o en Codex) y ejecuta `/empezar` (en Codex, `$empezar`). No hay dependencias que instalar para empezar.

## Primeros pasos

1. **Clona el repositorio** en una carpeta de trabajo.
2. **Ábrelo en Claude Code o Codex** y ejecuta `/empezar`.
   - Responde las 7 preguntas con honestidad. Las muestras de voz se pegan, no se describen.
   - Toma unos 15 minutos y, al final, se generan tus archivos del Día 1.
3. **Úsalo durante una semana.** Trae preguntas reales y toma decisiones reales. Pídele al asistente que registre las decisiones importantes en `decisions/log.md`.
4. **Día 7:** ejecuta `/auditar`. Lee el reporte de brechas de las Cuatro C y elige una brecha para cerrar.
5. **Día 14:** ejecuta `/subir-nivel`. La entrevista de las 3 M encuentra una automatización que vale la pena construir. Constrúyela.
6. **A medida que creces:**
   - usa `/entrevistame` para capturar contexto nuevo;
   - usa `/conectar` para agregar fuentes nuevas;
   - usa `/subir-nivel` para hacer una mejora a la vez;
   - vuelve a ejecutar `/auditar` para verificarla.

---

## La prueba de fuego

> **"Mientras no estás en tu escritorio, tu AIOS observa un evento real y produce un resultado más rápido y más preciso que el que producirías tú."**

Cada decisión de diseño del kit apunta a esa prueba. Si una capa, un skill o una plantilla no contribuye a ella, no se incluye.

## Cómo saber que está funcionando

Tres **indicadores de éxito** te dicen que el AIOS realmente está cambiando tu forma de trabajar. No son KPIs ni hay una métrica objetiva: son experiencias que aparecen en tu semana.

1. **El equipo te consulta.** Alguien de tu equipo te hace una pregunta y te das cuenta de que tu AIOS la respondería mejor, más rápido y con fuentes exactas. Ahí dejas de ser el cuello de botella de tu propio conocimiento.
2. **Menos cambio de contexto.** Dejas de abrir pestañas nuevas. Cuando llega algo nuevo, tu primer movimiento es preguntarle al AIOS, no abrir seis cosas.
3. **El conocimiento sale de tu cabeza.** Dejas de intentar recordar datos del negocio. Confías en la recuperación: el AIOS guarda la verdad y tú guardas las preguntas.

**De la base personal a una empresa lista para la IA.** Cuando estos indicadores aparecen en una persona, la misma arquitectura de datos sirve para todo lo demás:
- tableros sobre los datos que ya recopilas;
- automatizaciones sobre las conexiones que ya configuraste;
- un despliegue en el equipo, donde cada persona tiene el suyo.

---

## Dos frameworks

El kit enseña dos frameworks complementarios de Nate Herk: **primero las 3 M y después las Cuatro C.** Sin el cambio de mentalidad, la arquitectura es solo una estructura de carpetas.

### The Three Ms of AI™: tu forma de pensar como operador

| M | En una línea |
|---|---|
| **Mentalidad** (Mindset) | Default Shift, Function Breakdown, Curiosity Rule. *¿Hasta qué punto se puede aprovechar la IA aquí?* |
| **Método** (Method) | Encontrar la restricción → EAD (Eliminar, Automatizar, Delegar) → Mapear el proceso → Elegir el nivel de autonomía → Relacionarlo con un KPI. |
| **Máquina** (Machine) | Lego Principle, Validation Chain, Bike Method, Intern Rule, Kill Switch. *Lo aburrido es bello. Los flujos de trabajo le ganan a los agentes.* |

La explicación completa está en `references/3ms-framework.md`, y `/subir-nivel` te guía por las tres capas cada semana.

> *The Three Ms of AI™ es una marca registrada de Nate Herk. © 2026 Nate Herk.*

### The Four Cs of an AI OS™: la arquitectura (lo que construyes)

| # | Capa | En una línea | Prueba de "esta capa está lista" |
|---|---|---|---|
| 1 | **Contexto** (Context) | Conoce tu negocio | Una sesión nueva responde "¿qué hace este negocio y quién trabaja aquí?" sin buscar |
| 2 | **Conexiones** (Connections) | Llega a tus cosas | "¿Qué tengo mañana en el calendario y qué tareas vencen?" → datos en vivo, sin copiar y pegar |
| 3 | **Capacidades** (Capabilities) | Sabe hacer el trabajo | Una frase corta dispara un flujo de varios pasos que produce un artefacto |
| 4 | **Cadencia** (Cadence) | Funciona sin que se lo pidas | Con la laptop cerrada, llega un resumen al correo, o alguien del equipo le escribe y recibe una respuesta real |

> *The Four Cs of an AI OS™ es una marca registrada de Nate Herk. © 2026 Nate Herk.*

**Orden de las capas:**
- El Contexto no se puede saltar.
- Las Conexiones y las Capacidades se pueden construir en paralelo.
- La Cadencia va al final: no automatices flujos que no funcionan a mano.

---

## Qué incluye: 6 skills

| Comando (Claude Code) | Codex | Tipo | Cuándo usarlo |
|---|---|---|---|
| `/empezar` | `$empezar` | Asistente de configuración (una vez) | El Día 1, justo después de clonar. Entrevista de 7 preguntas. Genera los archivos del Día 1 y completa los manuales compartidos `CLAUDE.md` y `AGENTS.md`. |
| `/entrevistame` | `$entrevistame` | Entrevista de contexto guardada | Cuando quieras desarmar un plan o agregar contexto. Hace una pregunta a la vez y guarda cada respuesta en `brainstorms/`. |
| `/auditar` | `$auditar` | Revisión basada en evidencia | Después de la configuración, después de un arreglo importante y cada semana mientras construyes. Revisa el enrutamiento, la vigencia y la compatibilidad Claude/Codex, puntúa la confiabilidad verificada y guarda automáticamente un reporte fechado. |
| `/conectar` | `$conectar` | Ayudante de enrutamiento | Al agregar un proyecto, archivo, carpeta o fuente importante. Agrega la ruta más pequeña y útil al manual o índice y verifica que funcione. |
| `/subir-nivel` | `$subir-nivel` | Skill de pensamiento recurrente | El Día 14 y después cada semana. Entrevista de las 3 M (Mentalidad → Método → Máquina). Una ejecución = un artefacto entregado. |
| `/cerebro-3d` | `$cerebro-3d` | Explorador de conocimiento interactivo | Elige el nombre y las categorías de tu cerebro. Construye un globo 3D local con tus archivos, con búsqueda, lector de notas, modo cine y una repetición del crecimiento. |

### Comandos renombrados respecto de AIS-OS

Claude Code toma el nombre del comando de la carpeta del skill y no admite aliases. Por eso los comandos originales **ya no funcionan** en esta distribución. Si vienes de AIS-OS, usa esta tabla:

| AIS-OS (original) | Andromeda AI |
|---|---|
| `/onboard` | `/empezar` |
| `/audit` | `/auditar` |
| `/grill-me` | `/entrevistame` |
| `/link` | `/conectar` |
| `/level-up` | `/subir-nivel` |
| `/3d-brain` | `/cerebro-3d` |

La carpeta que genera el Cerebro 3D sigue siendo `apps/3d-brain/`, para que las instalaciones existentes sigan funcionando.

### Más sobre cada skill

**`/auditar`:**
- **Qué mide:** si el AIOS puede encontrar su información y hacer trabajo útil de forma confiable. El puntaje mide la confiabilidad operativa verificada, no la utilidad general.
- **Cómo puntúa:** la rúbrica v2 da puntos por evidencia, no por cantidad de carpetas, claves de API ni skills llamados "diarios". Las capas faltantes o sin verificar limitan el total; los skills instalados no compensan la falta de conexiones ni de historial de ejecución.
- **Qué incluye el reporte:**
  - cinco pruebas de recuperación;
  - revisiones de cachés desactualizadas y de autoridad de las fuentes;
  - diferencias entre manuales operativos;
  - compatibilidad de los paquetes de skills;
  - hasta tres mejoras priorizadas.

  Separa los defectos confirmados, las brechas de verificación, las diferencias intencionales entre runtimes y las mejoras opcionales.

**Historial automático de auditorías:** cada `/auditar` guarda un reporte Markdown fechado y único en `audits/`, y lo compara con los reportes anteriores relevantes.
- **Seguimiento de hallazgos:** conservan su ID y se clasifican como nuevo, sigue abierto, resuelto, reabierto, sin revisar o ya no aplica. Resolver uno requiere evidencia nueva.
- **Comparaciones de puntaje:** distinguen los arreglos reales de la mejor evidencia y de los cambios de cobertura.
- **Qué se escribe:** los reportes anteriores se conservan, y el sistema inspeccionado no cambia salvo por el reporte local nuevo.
- **Privacidad:** los reportes están en `.gitignore` porque pueden contener contexto privado. Una solicitud explícita de no guardar tiene prioridad.

**`/conectar ruta/al/proyecto "para qué usarlo"`:**
- Hace que una fuente nueva se pueda encontrar sin copiar su contenido al manual.
- Sigue las convenciones existentes de `AGENTS.md`/`CLAUDE.md` y solo pregunta cuando el destino o su uso no están claros.
- Estos skills nunca crean una caché "caliente".

**`/entrevistame "ayúdame a explicar cómo funciona mi negocio"`:** convierte lo que tienes en la cabeza en contexto guardado.
- Cada respuesta se guarda al instante en un archivo Markdown fechado en `brainstorms/`, así que puedes pausar y retomar.
- Cuando pides construir o actualizar el contexto del AIOS, los hechos confirmados se agregan a las páginas de contexto correspondientes, con enlaces a la entrevista. Las ideas tentativas quedan marcadas.
- Las capturas están en `.gitignore` por defecto.

**`/subir-nivel`:** lleva la evidencia de la auditoría a una sola mejora.
- Una reparación verificada de un flujo existente cuenta como resultado: no siempre hace falta otro skill nuevo.
- Después del arreglo, vuelve a ejecutar `/auditar`.
- El puntaje por uso repetido y ejecuciones programadas viene de la ejecución real a lo largo del tiempo.

---

## Tu Segundo Cerebro en 3D

Convierte tu colección de notas, proyectos y memorias del asistente en un solo lugar que puedes explorar:
- ve qué ideas se conectan;
- busca algo que recuerdas y abre la nota original;
- detecta el conocimiento que necesita atención.

La repetición del crecimiento también te sirve para mostrarle a alguien qué contiene tu AIOS.

[![El Cerebro 3D creciendo de una idea a un globo de conocimiento conectado (demo original de AIS-OS, en inglés)](docs/media/3d-brain-preview.gif)](https://github.com/nateherkai/AIS-OS/raw/refs/heads/main/docs/media/3d-brain-demo.mp4)

La vista previa muestra la secuencia completa de crecimiento. **[Descarga el video original de 36 segundos](https://github.com/nateherkai/AIS-OS/raw/refs/heads/main/docs/media/3d-brain-demo.mp4)** para verlo en resolución completa. Esa grabación es del proyecto original: muestra el "HerkBrain" de Nate, con la interfaz en inglés. En Andromeda AI la interfaz está en español, y el skill construye el tuyo con el nombre, las categorías y el conocimiento que elijas.

### Cómo funciona

1. **Ejecuta el skill:** `/cerebro-3d` en Claude Code o `$cerebro-3d` en Codex.
2. **Elige el nombre y las categorías.** El skill te pregunta cómo llamar a tu cerebro y qué categorías mostrar, y sugiere carpetas de origen.
3. **Se genera la app.** Con la plantilla incluida, el skill crea `apps/3d-brain/`. Tu nombre, categorías, colores y rutas quedan en un `brain.config.json` local.
4. **Se construye el grafo.** `node build.mjs` lee tus archivos Markdown y de texto, detecta los enlaces explícitos, los wikilinks y las menciones por título, y genera `data/graph.json`.
5. **Se abre el servidor.** `node serve.mjs` levanta un servidor local de solo lectura en `127.0.0.1` (puerto 4640 por defecto). Abre el enlace que aparece en la consola.

### Uso

- **Arrastra** para girar y **desplázate** para hacer zoom. Haz clic en un nodo para leer la nota. La tecla `/` activa la búsqueda.
- **Fuentes:** activa o desactiva categorías. Con Shift + clic ves solo una.
- **Qué hay aquí:** abre el inventario, con conteos, avisos y notas que requieren atención (desactualizadas, huérfanas, con enlaces rotos o borradores).
- **Reproducir demo** (`D`): el cerebro crece desde una sola idea siguiendo las conexiones reales, en unos 29 segundos. Es una repetición de la conectividad, no una línea de tiempo histórica.
- **Modo cine** (`C`): vista limpia para presentar o grabar. Escape la cierra.

Lee Markdown, texto y, de forma opcional, la memoria curada de Codex. La memoria de Claude, las notas de reuniones y el conocimiento de videos pueden venir de carpetas Markdown seleccionadas. Otros formatos o servicios en línea necesitan una exportación o un adaptador probado. La app queda en localhost, y la configuración personal y los datos generados están en `.gitignore`.

El renderer viene precompilado, así que la app funciona sin instalar dependencias. Si modificas el código del renderer (`src/`), ejecuta `npm ci` y `npm run build:js` en la carpeta de la plantilla o de la app.

El [paquete completo del skill](.claude/skills/cerebro-3d/README.md) incluye el código fuente, el bundle del navegador, la documentación de configuración, los avisos de licencias y un script de validación con datos ficticios:

```bash
node .claude/skills/cerebro-3d/scripts/test-package.mjs
```

---

## Personalización

- **Tu contexto:** edita `aios-intake.md` y vuelve a ejecutar `/empezar`. Los archivos de `context/`, `references/voice.md`, `connections.md` y `CLAUDE.md`/`AGENTS.md` se actualizan, y los originales se respaldan en `archives/`.
- **Tu voz y tus reglas de trabajo:** edita las secciones "Voz" y "Cómo trabajas conmigo" de `CLAUDE.md` y copia el mismo cambio en `AGENTS.md`.
- **El Cerebro 3D:** edita `apps/3d-brain/brain.config.json` (nombre, categorías, colores, rutas, puerto) y usa "Reconstruir desde el disco" en el inventario. La referencia de campos está en [config.md](.claude/skills/cerebro-3d/references/config.md).
- **Textos de la interfaz 3D:** están en `.claude/skills/cerebro-3d/assets/template/index.html` y `src/app.js`. Después de editar, recompila con `npm run build:js` (desde `assets/template/`) y sincroniza la copia de Codex.
- **Skills:** `.claude/skills/` es la fuente canónica. Después de editar un skill, ejecuta:

  ```bash
  bash scripts/sync-codex-skills.sh <nombre-del-skill>
  ```

  Para crear skills nuevos, usa `/subir-nivel`. Nombra las carpetas en minúsculas, sin tildes y con guiones: el nombre de la carpeta es el comando.

## Cómo agregar tu propio contenido

- **Frameworks y metodologías propias de Andromeda AI:** `references/andromeda/frameworks/`.
- **Conocimiento propio (guías, casos, lecciones):** `references/andromeda/conocimiento/`.
- **Qué hacer después de agregarlo:** usa `/conectar references/andromeda/... "cuándo usarlo"` para que el AIOS lo encuentre, e inclúyelo como categoría en tu Cerebro 3D.

Las instrucciones y las convenciones están en [references/andromeda/README.md](references/andromeda/README.md). Mantener este contenido separado de `references/3ms-framework.md` evita mezclar frameworks de terceros con los tuyos.

Consulta `EXPANSIONS.md` para ver qué más agregar a medida que creces (`projects/`, `templates/`, `scripts/`, `.claude/agents/`, carpetas de sub-OS, etc.).

---

## Uso con Codex

Los seis skills también están en `.agents/skills/`. Usa el selector de skills (`/skills` en Codex CLI o en la extensión de IDE), o escribe `$` y elige `empezar`, `auditar`, `entrevistame`, `conectar`, `subir-nivel` o `cerebro-3d`. Codex suele detectar los cambios en los skills automáticamente; si la lista no se actualiza, reinícialo.

`.claude/skills/` sigue siendo la fuente de edición. `scripts/sync-codex-skills.sh` regenera la copia de Codex, los archivos de apoyo y los metadatos del menú, cambiando solo las rutas `.claude/skills/` → `.agents/skills/` en los archivos `.md`. La plantilla del cuestionario de `empezar` y el framework de `subir-nivel` viajan con sus skills; los proyectos existentes conservan sus propias rutas de contexto canónicas.

---

## Estructura del repositorio

```
andromeda-ai/
├── README.md                        ← Este archivo
├── NOTICE.md                        ← Procedencia, autoría y marcas
├── LICENSE                          ← Licencia MIT original (sin cambios)
├── CLAUDE.md                        ← Manual operativo compartido para Claude Code
├── AGENTS.md                        ← Manual operativo equivalente para Codex
├── EXPANSIONS.md                    ← Qué agregar a medida que creces
├── .gitignore
├── aios-intake.md                   ← Fuente de verdad de /empezar. Edita y vuelve a ejecutar.
├── connections.md                   ← Registro de todos los sistemas que alcanza tu AIOS
├── context/                         ← Sobre ti y tu negocio (lo llena /empezar)
├── references/
│   ├── 3ms-framework.md             ← The Three Ms of AI™ (traducido, de Nate Herk)
│   └── andromeda/                   ← Frameworks y conocimiento propios de Andromeda AI
├── decisions/
│   └── log.md                       ← Registro de decisiones y sus razones
├── archives/                        ← Lo viejo. No lo borres: muévelo aquí.
├── brainstorms/                     ← Lo crea /entrevistame; entrevistas guardadas (ignorado por git)
├── audits/                          ← Se crea en la primera auditoría; reportes privados (ignorado por git)
├── docs/
│   ├── andromeda/                   ← Notas de la adaptación (baseline y verificación)
│   └── media/                       ← Demo original del Cerebro 3D (de AIS-OS)
├── scripts/sync-codex-skills.sh     ← Regenera las copias de skills para Codex
├── .agents/skills/                  ← Copias para Codex de los seis skills
└── .claude/
    └── skills/
        ├── empezar/
        ├── auditar/
        ├── entrevistame/
        ├── conectar/
        ├── subir-nivel/
        └── cerebro-3d/              ← Skill, plantilla de la app, documentación y scripts de validación
```

### Qué se mantuvo en inglés a propósito

Para no romper la compatibilidad, estos elementos técnicos no se tradujeron:
- los nombres de carpetas (`context/`, `references/`, `decisions/`, `brainstorms/`, `audits/`, `archives/`, `apps/3d-brain/`);
- las claves de `brain.config.json` y los tipos de adaptador (`markdown`, `codex-memory`);
- las claves YAML de los reportes de auditoría;
- los IDs de criterio de la rúbrica;
- los endpoints `/api/*` y el nombre del paquete `aios-3d-brain`.

---

## Licencia y procedencia

- **Software original:** [AIS-OS](https://github.com/nateherkai/AIS-OS), licencia MIT, © 2026 Nate Herk. El archivo [LICENSE](LICENSE) se conserva sin cambios.
- **Adaptación:** localización al español, renombre de comandos y branding Andromeda AI por Miguel Silva. Los cambios se pueden revisar en el historial de git de esta rama.
- **Marcas:** The Three Ms of AI™ y The Four Cs of an AI OS™ son marcas registradas de Nate Herk. Ambos frameworks se incluyen con atribución. El autor original pide: úsalos libremente, pero no los presentes como propios.
- **Marca Andromeda AI:** identifica esta distribución y no implica ninguna afiliación ni respaldo de Nate Herk o de AI Automation Society.
- **Dependencias de terceros del Cerebro 3D:** sus licencias están en [THIRD-PARTY-NOTICES.txt](.claude/skills/cerebro-3d/assets/template/THIRD-PARTY-NOTICES.txt).

Más detalles en [NOTICE.md](NOTICE.md).
