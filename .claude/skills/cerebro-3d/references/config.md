# Personalización y configuración de fuentes

Cuando el usuario elija el nombre y las categorías, crea un objeto JSON como este:

```json
{
  "name": "Cerebro de Atlas",
  "port": 4640,
  "sources": [
    {"id":"conocimiento","label":"Conocimiento del negocio","paths":["context","wiki"],"color":"#38BDF8","staleDays":75},
    {"id":"reuniones","label":"Reuniones","paths":["meetings"],"color":"#FB923C","staleDays":null},
    {"id":"proyectos","label":"Proyectos","paths":["projects"],"color":"#34D399"}
  ]
}
```

Es un ejemplo del esquema, no una autorización para suponer que esas carpetas existen. Incluye solo rutas verificadas y elegidas. El scaffold calcula `root` en relación con la app generada, así el AIOS puede moverse de carpeta o de equipo sin romper sus rutas internas. El `brain.config.json` local está en `.gitignore`.

Las claves del JSON (`name`, `sources`, `paths`, etc.) se mantienen en inglés porque forman parte del formato de datos. Los valores visibles (`name`, `label`) pueden ir en español.

Campos:

| Campo | Significado |
|---|---|
| `name` | Nombre exacto que se muestra, de 1 a 64 caracteres. Todo el branding personal sale de aquí. |
| `root` | Raíz del AIOS, relativa a la configuración de la app instalada. El scaffold la define automáticamente. |
| `port` | Puerto local, entre 1024 y 65535. Por defecto, 4640. Revisa que no esté ocupado. |
| `maxNodes` | Límite de escaneo. Por defecto, 3000; máximo, 10000. Si se alcanza, aparece un aviso en el inventario. |
| `sources` | Entre 1 y 12 categorías. |
| `sources[].id` | ID único en minúsculas que empieza con una letra. Solo letras (sin tildes ni ñ), dígitos y guiones. |
| `sources[].label` | Nombre de la categoría que ve el usuario. |
| `sources[].paths` | Archivos o carpetas aprobados, relativos a la raíz del AIOS, o rutas absolutas o con `~/` explícitas. No acepta patrones glob. |
| `sources[].type` | `markdown` (por defecto) o `codex-memory`. |
| `sources[].color` | Opcional. Color hexadecimal de seis dígitos; si no se indica, se asigna un color distinto de la paleta. |
| `sources[].exclude` | Opcional. Prefijos de rutas relativas dentro de cada carpeta seleccionada. |
| `sources[].staleDays` | Número positivo; por defecto, 90. `null` desactiva el aviso de desactualización para registros históricos. |
| `sources[].obsidianVault` | Opcional. Nombre de una bóveda de Obsidian existente. Úsalo solo si las rutas de los nodos son válidas dentro de la bóveda. |

## Fuentes compatibles

**Markdown:** escanea `.md` y `.txt` de forma recursiva, lee el frontmatter escalar simple (`title`, `name`, `description`, `type`, `updated`, `created`, `tags`) y resuelve enlaces Markdown a archivos y wikilinks. Lo que se incluye depende de la estructura de carpetas de la fuente, no de una organización de wiki fija. Las entradas del índice de proyectos quedan como texto de la nota: para incluir las notas de un proyecto, hay que seleccionar su carpeta.

Se excluyen las carpetas ocultas, git, las dependencias, los archivos archivados, las carpetas temporales, las salidas de auditoría, los datos generados y la propia app generada. Los enlaces simbólicos se omiten durante el escaneo. Los archivos de más de 1 MB generan un aviso. Las notas de navegación se listan en el inventario en lugar de dibujarse. Elegir el mismo archivo dos veces no duplica su nodo.

**Memoria de Claude:** usa `markdown` con la carpeta de memoria de Claude del proyecto, previamente aprobada. No inventes el nombre codificado de esa carpeta: verifícalo en el equipo actual. El descubrimiento ofrece la coincidencia exacta con la raíz actual, si existe.

**Memoria de Codex:** usa `codex-memory` con una raíz de memoria elegida explícitamente. El descubrimiento respeta `CODEX_HOME`; si no existe, revisa `~/.codex/memories`. El adaptador lee `memory_summary.md`, las secciones de `MEMORY.md`, los `rollout_summaries/` en Markdown, los `skills/` de la memoria y `extensions/ad_hoc/notes/`. No escanea conversaciones sin procesar, `.env`, credenciales, archivos ocultos ni el duplicado `raw_memories.md`. Esa memoria puede contener recuerdos de varios proyectos, así que el usuario debe conocer ese alcance antes de elegirla.

**Otros formatos:** no son compatibles por defecto. Pide o crea una exportación local en Markdown autorizada, o implementa un adaptador documentado. No inventes contenido de negocio faltante ni digas que hay cobertura de APIs remotas.
