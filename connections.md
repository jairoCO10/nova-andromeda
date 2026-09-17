# Conexiones

Registro de todos los sistemas a los que puede acceder tu AIOS. `/empezar` lo llena con las respuestas de P4 a P7 y va creciendo a medida que conectas herramientas nuevas. `/auditar` revisa este archivo para comprobar la cobertura de dominios y qué tan actualizado está.

| # | Dominio | Herramienta | Mecanismo | Autenticación | Última revisión |
|---|---|---|---|---|---|
| 1 | Ingresos / Finanzas | _lo llena /empezar_ | aún no conectado | — | — |
| 2 | Interacciones con clientes | _lo llena /empezar_ | aún no conectado | — | — |
| 3 | Calendario | _lo llena /empezar_ | aún no conectado | — | — |
| 4 | Comunicación | _lo llena /empezar_ | aún no conectado | — | — |
| 5 | Seguimiento de proyectos / tareas | _lo llena /empezar_ | aún no conectado | — | — |
| 6 | Inteligencia de reuniones | _lo llena /empezar_ | aún no conectado | — | — |
| 7 | Conocimiento / archivos | _lo llena /empezar_ | aún no conectado | — | — |

**Opciones de mecanismo:**
- `mcp`: servidor MCP.
- `script`: Python o Bash que consulta una API, guardado en `scripts/`.
- `export`: flujo de exportación CSV/JSON.
- `key+ref`: clave en `.env` + guía en `references/{herramienta}-api.md`.
- `aún no conectado`.

Los identificadores de mecanismo se mantienen en inglés porque `/auditar` los reconoce así.

Cuando conectes una herramienta nueva, guarda también `references/{herramienta}-api.md` con los endpoints, el flujo de autenticación y las consultas comunes: lo investigas una vez y queda guardado para siempre.
