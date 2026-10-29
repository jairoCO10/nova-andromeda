# Aviso de procedencia y atribución

## Software original

Esta distribución es una obra derivada de **AIS-OS** (AI Automation Society OS):

- Repositorio: https://github.com/nateherkai/AIS-OS
- Autor: **Nate Herk**
- Licencia: MIT, © 2026 Nate Herk. El texto completo está en [LICENSE](LICENSE), que se conserva sin modificaciones.
- Base de la adaptación: commit `ce9cb93` ("Add Grill Me interviews for ongoing AI OS context").

La arquitectura, el código, los skills, el renderer del Cerebro 3D y los frameworks son obra original de Nate Herk. El aviso de copyright y el permiso MIT deben acompañar todas las copias o partes sustanciales del software.

## Marcas del autor original

- **The Three Ms of AI™** es una marca registrada de Nate Herk. El contenido de `references/3ms-framework.md` se comparte bajo los mismos términos MIT (según `LICENSE`), pero el nombre de la marca está reservado. En esta distribución se conserva el nombre original y se agrega una glosa descriptiva en español ("las 3 M": Mentalidad, Método, Máquina).
- **The Four Cs of an AI OS™** es una marca registrada de Nate Herk (según el README original). En español se usa "las Cuatro C" como glosa descriptiva.
- El autor original pide: úsalos libremente, pero no los presentes como propios.

## Adaptación Andromeda AI

- **Marca de la distribución:** Andromeda AI.
- **Adaptación y localización:** Miguel Silva (2026).
- **Qué cambió:**
  - traducción al español latinoamericano de la interfaz del Cerebro 3D, los mensajes de los scripts, los skills, las plantillas y la documentación;
  - renombre de los comandos (ver la tabla abajo);
  - branding discreto ("Andromeda AI · adaptado por Miguel Silva") en la pantalla de inicio y en el título del Cerebro 3D;
  - espacio para contenido propio en `references/andromeda/`.
- **Qué no cambió:** la arquitectura, los formatos de datos, la lógica 3D y las dependencias.
- **Detalle de los cambios:** el historial de git de la rama `andromeda`, a partir del commit base indicado arriba.

Andromeda AI identifica esta distribución. **No implica afiliación, patrocinio ni respaldo** de Nate Herk ni de AI Automation Society. Miguel Silva no es el autor del código original.

### Cambio incompatible: comandos renombrados

Claude Code toma el nombre de un skill de proyecto de su carpeta y no admite aliases. Los comandos originales no están disponibles en esta distribución:

| AIS-OS | Andromeda AI |
|---|---|
| `/onboard` | `/empezar` |
| `/audit` | `/auditar` |
| `/grill-me` | `/entrevistame` |
| `/link` | `/conectar` |
| `/level-up` | `/subir-nivel` |
| `/3d-brain` | `/cerebro-3d` |

## Componentes de terceros

- **Renderer del Cerebro 3D** (`.claude/skills/cerebro-3d/assets/template/dist/app.js`, y su copia en `.agents/`): empaqueta three, 3d-force-graph, marked, DOMPurify, d3 y otras dependencias.
  - Sus licencias (MIT, ISC, tipo BSD y la licencia dual Apache-2.0 / MPL-2.0 de DOMPurify) están en `THIRD-PARTY-NOTICES.txt`, que se conserva sin cambios junto al bundle.
  - Si agregas o actualizas dependencias, actualiza ese archivo.
- **Tipografía del Cerebro 3D:** NOVA usa las fuentes del sistema y quitó las llamadas remotas a Google Fonts para mantener la interfaz local.
- **Demo en video** (`docs/media/3d-brain-demo.mp4` y `3d-brain-preview.gif`): es la grabación original del autor (el "HerkBrain" de Nate Herk, con la interfaz en inglés). Se conserva sin cambios y con atribución. Conviene reemplazarla por una grabación propia de Andromeda AI antes de usarla con fines promocionales.

## Contenido propio de Andromeda AI

Los frameworks y el conocimiento originales de Andromeda AI van en `references/andromeda/`. Ese contenido es de Miguel Silva y puede tener sus propios términos, que se indicarán en cada archivo. Mientras no se indique otra cosa, se distribuye junto con este repositorio bajo la misma licencia MIT.

## Adaptación NOVA

Este repositorio es un fork de Andromeda AI adaptado para NOVA por Jairo Cogollo Otero. La adaptación integra una consola Python con Ollama y SQLite, incorpora comandos locales para las entrevistas y auditorías, y cambia el branding del Segundo Cerebro 3D a NOVA. El renderer 3D y los frameworks derivados conservan la procedencia y licencias de sus autores originales; esta adaptación no implica afiliación ni respaldo de Nate Herk, AI Automation Society o Miguel Silva.
