# Validación de la adaptación Andromeda AI

Fecha: 2026-09-17 · Windows 11 · Node.js 22.16.0 · npm 10.9.2

## Automatizada

| Verificación | Resultado |
|---|---|
| `test-package.mjs` en `.claude` y `.agents` | OK (8 notas) |
| `test-package.mjs --demo` en `.claude` y `.agents` | OK (188 notas) |
| `npm ci` + `npm run build:js` | OK; `dist/app.js` regenerado desde `src/` |
| `diff -r .claude/skills .agents/skills` | Solo difieren las rutas transformadas por `sync-codex-skills.sh` |
| `CLAUDE.md` frente a `AGENTS.md` | Idénticos |
| `LICENSE` y `THIRD-PARTY-NOTICES.txt` | Sin cambios de contenido (el segundo solo cambió de carpeta) |
| Lint / typecheck | No existen en el proyecto (igual que en upstream) |

## Navegador (panel integrado)

**Fixture "Atlas Brain" (188 notas), escritorio y 406 px.** Funcionaron:
- la pantalla de inicio con la marca, el inventario y el panel de nota;
- la búsqueda sin resultados, el filtro de una fuente y su restauración;
- la pausa de movimiento;
- la demo completa (1 → 18 → 188/188, "Repetir demo") y el modo cine.

No hubo errores de consola.

## Smoke test desde cero

1. Se hizo `git clone -b andromeda` en un directorio temporal limpio (sin `node_modules`).
2. Se ejecutaron `discover.mjs`, luego `scaffold.mjs` (configuración en español: "Cerebro de Lucía", categorías "Mi negocio", "Andromeda AI" y "Decisiones") y después `build.mjs` (6 notas, 3 conexiones, 3 categorías) y `serve.mjs`.
3. Resultados:
   - `brain.config.json` quedó con `root: "../.."` (relativo), sin dependencias del repositorio de desarrollo.
   - El renderer cargó sin instalar dependencias.
   - Funcionaron el título con la marca, el lector de notas con su frontmatter, el enlace a un archivo relativo, la mención por título y el inventario.
   - No hubo errores de consola.

**Limitación:** durante el smoke test, el panel del navegador dejó de entregar fotogramas (una medición directa de `requestAnimationFrame` en la página no registró ningún fotograma en 3 segundos), así que no se pudo observar la animación de la demo en ese cerebro pequeño. La demo se verificó completa con el mismo bundle en el fixture de 188 notas, y la lógica de crecimiento está cubierta por `test-package.mjs`.

## Pendiente de verificar

- Una ejecución conversacional real de cada skill (`/empezar`, `/auditar`, `/entrevistame`, `/conectar`, `/subir-nivel`, `/cerebro-3d`) en Claude Code y en Codex.
- macOS y Linux.
- Grafos en el máximo configurado.
