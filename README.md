# NOVA + Andromeda AI

NOVA es un asistente personal local que usa Ollama y SQLite. Este fork integra los flujos de contexto de Andromeda AI y su **Segundo Cerebro 3D**, adaptados para que NOVA los pueda ejecutar desde su consola.

## Qué puedes hacer

- Hablar con el modelo local de Ollama y conservar recuerdos y planes en SQLite.
- Usar `/mantenimiento` para rehacer el perfil personal con un formulario local y copia de seguridad.
- Consultar la hora local del equipo sin depender del modelo ni de Internet.
- Usar `/empezar` para configurar el contexto que NOVA consulta.
- Usar `/entrevistame` para explorar una idea y guardar la sesión localmente.
- Usar `/conectar` para registrar una ruta o fuente sin copiar su contenido.
- Usar `/auditar` para revisar el contexto, las fuentes y las capacidades disponibles.
- Usar `/subir-nivel` para diseñar una mejora de flujo de trabajo con las 3 M.
- Usar `/cerebro-3d` para crear y abrir el grafo interactivo local.

El cerebro conserva el renderer 3D de Andromeda: esfera de conocimiento, búsqueda, filtros por categoría, lector de notas, inventario, modo cine y demo de crecimiento.

## Requisitos

- Python 3.10 o superior.
- Ollama con un modelo local llamado `nova` (o configura `NOVA_MODEL`).
- Node.js 22.x para el Segundo Cerebro 3D. El proyecto fija esa versión con `.nvmrc` y `.node-version`.

## Inicio

```bash
ollama serve
python3 app.py
```

En macOS, instala la versión aislada con `brew install node@22`. NOVA la detecta para el cerebro 3D y deja intacto el `node` global. En la consola de NOVA, escribe `/ayuda`; usa `/mantenimiento` para completar tu perfil y `/cerebro-3d` para elegir las carpetas del grafo. El cerebro se sirve solo en `127.0.0.1`.

## Datos locales y privacidad

Los recuerdos y planes viven en `data/nova.sqlite3`; el perfil está en `perfil/`; las entrevistas, decisiones y auditorías se guardan localmente. Esos archivos están excluidos de Git. El repositorio contiene instrucciones, ejemplos y el código base, no el perfil ni la memoria de una persona.

Para completar o rehacer el perfil, usa `/mantenimiento`. NOVA guarda una copia local oculta del perfil anterior antes de reemplazarlo; la memoria SQLite permanece separada. También puedes crear el perfil manualmente desde los archivos `perfil/*.example.md`.

El cerebro 3D lee solo las categorías y rutas que el usuario elige. No indexa SQLite, `perfil/`, copias de seguridad ni carpetas ocultas de forma predeterminada. `brain.config.json` y el grafo derivado también son locales y están excluidos de Git.

## Licencias y procedencia

Este repositorio deriva de [Andromeda AI](https://github.com/Miguel21313/andromeda-ai), a su vez basado en AIS-OS. Se conservan la licencia MIT, los avisos de procedencia y las licencias de las dependencias del Cerebro 3D. La adaptación NOVA agrega la integración con Ollama, SQLite y la consola local. Consulta [NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).
