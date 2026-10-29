# Andromeda integrado en NOVA

Los seis paquetes de Andromeda AI se conservan bajo `skills/`. Las instrucciones de cada paquete documentan el flujo original; la consola local de NOVA ejecuta sus equivalentes a través de `andromeda_runtime.py` y Ollama.

| Comando | Integración local |
|---|---|
| `/empezar` | Entrevista inicial y páginas privadas en `context/`, disponibles en el contexto de Ollama. |
| `/entrevistame` | Entrevista adaptativa, guardado por turno y resumen en `brainstorms/`. |
| `/conectar` | Registra rutas y propósito sin copiar ni leer fuentes. |
| `/auditar` | Revisa estructura y evidencia local de las Cuatro C. |
| `/subir-nivel` | Entrevista de las 3 M y propuesta de un flujo medible. |
| `/cerebro-3d` | Genera el grafo 3D incluido y lo sirve en loopback. |

El Cerebro 3D lee solo las carpetas elegidas en el asistente de configuración. Para instalarlo necesita Node.js 22 o superior; el resto de NOVA funciona con Python y Ollama.
