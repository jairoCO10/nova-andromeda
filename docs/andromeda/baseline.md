# Baseline upstream (antes de la adaptación)

Referencia: `nateherkai/AIS-OS` en el commit `ce9cb93`, verificado el 2026-09-17 en Windows 11 con Node 22.16.0 y npm 10.9.2.

| Verificación | Resultado |
|---|---|
| `node .claude/skills/3d-brain/scripts/test-package.mjs` | OK (8 notas) |
| `node .agents/skills/3d-brain/scripts/test-package.mjs` | OK (8 notas) |
| `test-package.mjs --demo` | OK (188 notas) |
| `npm ci` + `npm run build:js` en la plantilla | OK |
| Reproducibilidad de `dist/app.js` | **No idéntica.** El bundle recompilado difiere del incluido solo en directivas `"use strict"` dentro de módulos CommonJS empaquetados (1.661.570 vs. 1.661.538 bytes), por una versión de parche distinta de esbuild. Esto ya pasaba en upstream y no cambia el comportamiento. |
| `diff -r .claude/skills .agents/skills` | Solo cambian las rutas `.claude/skills/` → `.agents/skills/` en archivos `.md`. Esto confirma que `scripts/sync-codex-skills.sh` genera la copia de Codex a partir de `.claude/skills`, que es la fuente principal. |
| Lint / typecheck | El proyecto no los tiene. |

## Aliases de comandos

La documentación de Claude Code (code.claude.com/docs/en/skills) indica que en skills de proyecto el comando sale del **nombre de la carpeta** y que no hay aliases. Por eso, renombrar los skills al español rompe los comandos originales. Las equivalencias están en el README.
