# Contenido propio de Andromeda AI

Este es el espacio para los frameworks, metodologías y conocimiento originales de **Andromeda AI** (Miguel Silva). Está separado a propósito:

- de `references/3ms-framework.md`, que es un framework de terceros (The Three Ms of AI™, de Nate Herk);
- de `context/`, que describe a cada usuario y lo llena `/empezar`;
- del código y los skills del kit, que vienen de AIS-OS.

Así puedes actualizar tu contenido sin tocar el núcleo, y traer mejoras del proyecto original sin conflictos.

## Estructura

```
references/andromeda/
├── README.md              ← Este archivo
├── frameworks/            ← Frameworks y metodologías con nombre propio
│   └── README.md
└── conocimiento/          ← Guías, casos, lecciones y material de referencia
    └── README.md
```

## Cómo agregar contenido

1. Crea un archivo Markdown en la carpeta correspondiente, con un nombre en minúsculas y con guiones (por ejemplo, `frameworks/nombre-del-framework.md`).
2. Empieza con un encabezado `# Título` y, si quieres, frontmatter simple:

   ```markdown
   ---
   title: Nombre del framework
   description: Una línea sobre qué resuelve.
   updated: 2026-09-17
   tags: [andromeda, framework]
   ---
   ```

   El Cerebro 3D usa `title`, `description`, `updated` y `tags` para mostrar la nota.
3. Enlaza las notas entre sí con enlaces Markdown o wikilinks (`[[Otro framework]]`): así aparecen conectadas en el Cerebro 3D.
4. Hazlo encontrable para el AIOS:

   ```text
   /conectar references/andromeda/frameworks "cuando necesites aplicar un framework de Andromeda AI"
   ```

5. Opcional: agrega `references/andromeda` como categoría de tu Cerebro 3D (por ejemplo, con la etiqueta "Andromeda AI") y reconstruye el grafo.
6. Si un skill debe aplicar un framework propio, referencia su ruta desde el `SKILL.md` correspondiente, en lugar de copiar el contenido dentro del skill.

## Reglas

- No mezcles aquí contenido de terceros sin atribución.
- Indica en cada archivo quién es el autor y, si aplica, sus términos de uso.
- Los marcadores `[PENDIENTE: ...]` indican contenido que todavía no se ha escrito. No los reemplaces con contenido inventado.
