# NOVA + Andromeda AI

NOVA es un asistente personal local que usa Ollama y SQLite. Este fork integra los flujos de contexto de Andromeda AI y su **Segundo Cerebro 3D**, adaptados para que NOVA los pueda ejecutar desde su consola.

## Qué puedes hacer

- Hablar con el modelo local de Ollama y conservar recuerdos y planes en SQLite.
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
- Node.js 22 o superior únicamente para construir el Segundo Cerebro 3D.

## Inicio

```bash
ollama serve
python3 app.py
```

En la consola de NOVA, escribe `/ayuda` para ver los comandos. Para iniciar el cerebro 3D, escribe `/cerebro-3d`, elige un nombre y aprueba las carpetas que quieres indexar. La app se sirve solo en `127.0.0.1`; NOVA no sube notas a ningún servicio.

## Datos locales y privacidad

Los recuerdos y planes viven en `data/nova.sqlite3`; el perfil está en `perfil/`; las entrevistas, decisiones y auditorías se guardan localmente. Esos archivos están excluidos de Git. El repositorio contiene instrucciones, ejemplos y el código base, no el perfil ni la memoria de una persona.

Para crear un perfil nuevo, copia los archivos `perfil/*.example.md` que necesites y quita el sufijo `.example` en los archivos locales.

El cerebro 3D lee solo las categorías y rutas que el usuario elige. No indexa SQLite, `perfil/`, copias de seguridad ni carpetas ocultas de forma predeterminada. `brain.config.json` y el grafo derivado también son locales y están excluidos de Git.

## Licencias y procedencia

Este repositorio deriva de [Andromeda AI](https://github.com/Miguel21313/andromeda-ai), a su vez basado en AIS-OS. Se conservan la licencia MIT, los avisos de procedencia y las licencias de las dependencias del Cerebro 3D. La adaptación NOVA agrega la integración con Ollama, SQLite y la consola local. Consulta [NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).
