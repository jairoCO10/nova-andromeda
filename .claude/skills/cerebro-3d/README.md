# Skill Cerebro 3D

Construye un globo interactivo, con el nombre que tú elijas, a partir del conocimiento guardado en tu AIOS. El skill te pide el nombre del cerebro y sus categorías principales, relaciona cada categoría con carpetas locales que tú apruebas y crea la app incluida en `apps/3d-brain/`.

- Claude Code: `/cerebro-3d`
- Codex: selecciona **Cerebro 3D** o escribe `$cerebro-3d`
- Lenguaje natural: "Construye un cerebro 3D con mi AIOS."

Requiere Node.js 22 o superior. El renderer ya viene compilado, así que la app generada funciona con `node serve.mjs` sin instalar nada con npm. Si modificas el renderer, ejecuta `npm ci` y `npm run build:js` en la app generada.

La app incluye el globo, el orbe central, categorías con colores, búsqueda, lector de notas, filtros por fuente, inventario, modo cine y una repetición interactiva del crecimiento. Puedes arrastrar y hacer zoom mientras crece. Las conexiones salen de las notas seleccionadas: la animación muestra cómo se conectan, no cuándo se crearon.

Lee directamente Markdown y texto, y también la memoria curada de Codex. La memoria de Claude se lee desde la carpeta Markdown que elijas. El conocimiento de reuniones y videos puede venir de exportaciones en Markdown. Otros formatos y servicios en línea necesitan una exportación o un adaptador probado.

Para instalarlo por separado, copia esta carpeta completa (incluidas `assets`, `scripts`, `references` y `agents`) en `.claude/skills/cerebro-3d/` del AIOS de destino. En este repositorio, ejecuta `bash scripts/sync-codex-skills.sh cerebro-3d` para generar la copia de Codex. No copies solo `SKILL.md` ni incluyas la configuración o los datos generados de otra persona.

Validación del paquete: `node scripts/test-package.mjs`. Para una prueba visual más grande con datos ficticios, agrega `--keep --demo --out <carpeta-temporal>`.

Consulta [SKILL.md](SKILL.md) para ver el flujo, [la especificación portable](references/portable-spec.md) para el contrato de implementación y [la guía de configuración](references/config.md) para los adaptadores y límites.
