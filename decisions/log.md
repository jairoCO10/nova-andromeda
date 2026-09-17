# Registro de decisiones

Registro de solo anexar con las decisiones importantes y sus razones. La Fase 2 de `/subir-nivel` (entrevista de Método) escribe aquí las especificaciones de las automatizaciones definidas. También puedes agregar entradas a mano cada vez que decidas algo que valga la pena recordar.

**Formato de cada entrada:**

```
## AAAA-MM-DD — Título corto

**Decisión:** qué se decidió.

**Por qué:** el razonamiento, las restricciones y qué te haría cambiar de opinión.

**Alternativas consideradas:** qué otras opciones había.

**Responsable:** quién responde por la decisión.
```

Sé breve. Tu yo del futuro te agradecerá que hayas guardado el *por qué*, no solo el *qué*.

---

## 2026-09-17 - Adaptación Andromeda AI en español

**Decisión:** Distribuir AIS-OS como Andromeda AI, localizado al español latinoamericano neutro. Los comandos se renombran (`/empezar`, `/auditar`, `/entrevistame`, `/conectar`, `/subir-nivel`, `/cerebro-3d`) y se conservan la arquitectura, los formatos de datos, las rutas internas y la carpeta generada `apps/3d-brain/`.

**Por qué:** Los comandos en español son más fáciles de recordar para la audiencia latinoamericana. Claude Code toma el nombre del comando de la carpeta del skill y no admite aliases, así que el cambio rompe los nombres anteriores; la tabla de equivalencias está en el README.

**Alternativas consideradas:** Mantener los comandos en inglés y traducir solo la experiencia; tener skills duplicados como alias. El primero es menos memorable; el segundo agrega ambigüedad.

**Responsable:** Miguel Silva (adaptación). El software original es de Nate Herk (ver `NOTICE.md`).

## Decisiones heredadas del proyecto original (AIS-OS)

Las siguientes entradas son del autor original y se conservan traducidas. Los nombres de comandos se actualizaron a los de esta adaptación.

## 2026-09-06 - Evidencia de auditoría y mantenimiento del enrutamiento

**Decisión:** Publicar la rúbrica de auditoría v2 y un skill pequeño, `/conectar`. La auditoría puntúa la evidencia de funcionamiento en las Cuatro C, revisa el enrutamiento del manual operativo y su vigencia, y pasa una brecha concreta a `/subir-nivel`. Una reparación seleccionada puede mejorar un flujo de trabajo existente en lugar de crear otro skill.

**Por qué:** El número de archivos, las claves configuradas, los rituales con nombre y las ediciones recientes no prueban que un AIOS funcione. Encontrar las fuentes y saber si están al día requiere comprobaciones explícitas.

**Alternativas consideradas:** Mantener la puntuación por presencia de archivos o exigir una caché "caliente". Ninguna de las dos garantiza la calidad de la recuperación ni una ejecución exitosa.

## 2026-09-06 - Skills portables e historial automático de auditorías

**Decisión:** Publicar los skills para Claude Code y Codex, con sus recursos incluidos, manuales operativos equivalentes y un script para regenerar las copias de Codex. Los reportes de auditoría se guardan automáticamente, conservan las ejecuciones anteriores y dan seguimiento a los hallazgos entre revisiones comparables.

**Por qué:** Los estudiantes necesitan la misma guía compartida al cambiar de asistente, y evidencia de mejoras reales con el tiempo. Las adaptaciones intencionales de cada runtime, lo que no se pudo verificar y los defectos confirmados se reportan por separado.

## 2026-09-06 - Skill portable de Cerebro 3D

**Decisión:** Agregar `/cerebro-3d` para Claude Code y Codex. Pide un nombre y categorías, relaciona carpetas locales seleccionadas y genera una aplicación incluida y configurable con ubicación esférica, modo cine y repetición interactiva del crecimiento.

**Por qué:** Distribuir el renderer que ya funciona conserva la apariencia y las interacciones previstas en cualquier instalación del AIOS. Un prompt solo con texto produciría recreaciones inconsistentes. La configuración del usuario y los datos del grafo quedan en su equipo; el paquete público incluye solo código, documentación, avisos de dependencias y datos de prueba ficticios.

## 2026-09-06 - Entrevistas continuas de contexto

**Decisión:** Adaptar el skill grill-me de Herk-2 para el kit de estudiantes (en esta adaptación, `/entrevistame`) y publicar paquetes equivalentes para Claude y Codex. Guardar cada respuesta en `brainstorms/`, conservar un historial de preguntas y respuestas que se pueda retomar, y actualizar el contexto canónico solo con hechos confirmados durante las sesiones de construcción de contexto que se soliciten.

**Por qué:** El onboarding es una foto inicial. Las entrevistas continuas capturan prioridades, decisiones y preferencias que cambian, y mantienen las ideas tentativas separadas de los hechos actuales del negocio.
