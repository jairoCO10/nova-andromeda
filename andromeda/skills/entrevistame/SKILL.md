---
name: entrevistame
description: Entrevista al usuario a fondo sobre un plan, un diseño o un tema, y guarda cada respuesta en un archivo de brainstorm para que nada se pierda. Úsalo cuando el usuario quiera poner a prueba un plan, que lo cuestionen sobre un diseño, hacer una sesión de lluvia de ideas o descubrimiento, sacar a un documento lo que tiene en la cabeza, construir con el tiempo el contexto de su AIOS, o diga "entrevístame", "hazme preguntas", "ponme a prueba" o "grill me".
---

# Entrevístame

Entrevista al usuario a fondo sobre cada aspecto del tema hasta llegar a un entendimiento compartido. Recorre cada rama del árbol de decisiones y resuelve las dependencias una por una. El objetivo real es **sacar lo que el usuario tiene en la cabeza y llevarlo a un archivo Markdown durable y ordenado**, para que nada se pierda a medida que se llena el contexto.

Habla con el usuario en español latinoamericano neutro, salvo que prefiera otro idioma.

## El archivo de captura es lo más importante

Las entrevistas largas llenan el contexto. Si solo guardas las respuestas en tu memoria de trabajo, tarde o temprano vas a recordar algo mal, mezclar respuestas u olvidar algo. Por eso **guardas en disco después de cada respuesta**. La fuente de verdad es el archivo, no tu contexto. Nunca hagas que el usuario te pida guardar el avance.

## Contexto existente y alcance

- Lee el `AGENTS.md` y el `CLAUDE.md` que correspondan, y después solo las páginas de contexto y las capturas anteriores relacionadas con el tema.
- El contexto del kit base vive en `context/`. En un proyecto establecido, sigue sus rutas declaradas en lugar de crear un almacén de conocimiento duplicado.
- Reutiliza los datos que ya te dieron y pregunta por los vacíos, los cambios, las decisiones y las ventajas y desventajas de cada opción.
- Instalar el skill no inicia una entrevista.

## Preparación (hazla ANTES de la primera pregunta)

1. **Crea el archivo de captura** en `brainstorms/{AAAA-MM-DD}-{tema-en-slug}.md`. Si la carpeta `brainstorms/` no existe, créala.
   - Todas las capturas viven aquí, en un solo lugar predecible sin importar el tema. NO las repartas en carpetas de proyectos.
   - Si una sesión produce después un entregable pulido (un plan, un mapa, una especificación), ese artefacto puede moverse a la carpeta de `projects/` que corresponda, pero la captura original siempre queda en `brainstorms/`.
   - Obtén la fecha real de hoy con el reloj o la terminal disponibles (`Get-Date -Format yyyy-MM-dd` en PowerShell, `date +%F` en Bash).
   - Nunca sobrescribas una captura existente. Si es una sesión nueva con la misma fecha y tema, agrega la hora o un sufijo único y crea el archivo en modo exclusivo.
   - Retoma una captura existente solo si el usuario lo pide o se refiere claramente a esa sesión. En ese caso, léela primero y continúa su numeración de preguntas.
   - Si no hay un tema indicado ni deducible, crea una captura `descubrimiento-sin-titulo` con el objetivo pendiente y pregunta qué explorar. Registra el tema y el objetivo elegidos en ese mismo archivo.
2. **Crea el archivo de inmediato** con un encabezado: título, fecha, objetivo de la sesión y una sección vacía de "Pendientes abiertos".
3. **Dile al usuario dónde vas a guardar**, en una línea. Después haz la P1.

## La regla de guardado (no se negocia)

Después de CADA respuesta del usuario, ANTES de hacer la siguiente pregunta:
- Agrega al archivo de captura una entrada estructurada con:
  - el tema de la pregunta;
  - los datos y decisiones clave de la respuesta (con sus palabras cuando la redacción importe);
  - los pendientes: lo que no pudo responder y quién debería hacerlo.
- Actualiza el resumen general cuando una respuesta posterior lo cambie. Conserva la entrada original, márcala como reemplazada y enlázala a la respuesta que la corrige, para que el razonamiento se pueda rastrear.
- Relee la entrada guardada antes de continuar. Si falla el guardado, explica el error y deja la respuesta visible en el chat. No digas que se guardó ni sigas recopilando respuestas sin un guardado que funcione.
- Solo entonces haz la siguiente pregunta.

Nunca juntes varias respuestas en una sola escritura: guarda una respuesta a la vez. Así, si se pierde el contexto en cualquier momento, el archivo ya tiene todo lo dicho hasta ahí.

## Método de entrevista

- Haz **una pregunta a la vez**.
  - En las decisiones, ofrece una respuesta sugerida basada en el contexto y márcala como sugerencia.
  - En los datos personales o del negocio, pregunta de forma neutral: no induzcas al usuario con datos inventados ni guardes tu inferencia como si fuera su respuesta.
- En la captura, mantén distinguibles los hechos confirmados por el usuario, las ideas tentativas, las sugerencias del asistente y las preguntas sin resolver.
- Resuelve las dependencias en orden: define la decisión de base antes que las que dependen de ella.
- Si una pregunta se puede responder **explorando el código o leyendo un archivo o documento**, hazlo en lugar de preguntar. Si el usuario te da un documento (por ejemplo, un Google Doc), léelo y menciona solo lo que sea nuevo.
- Cuando el usuario **no pueda responder** algo, regístralo como pendiente con su responsable y sigue. No te estanques.
- Continúa hasta que el usuario diga que terminaste, necesite una pausa o hayas cubierto las ramas útiles.
  - Si el usuario pide parar explícitamente, respeta la pausa de inmediato y no agregues otra pregunta.
  - Cerca del final, haz una pregunta de cierre: "¿Hay algo que no hayamos tocado?".

## Estructura del archivo de captura

```
# {Tema}: notas de brainstorm / descubrimiento
Fecha: {fecha} · Objetivo: {una línea}
Estado: en curso / en pausa / completo
Fuentes de contexto: {páginas existentes relevantes, si hay}

## Resumen / decisiones clave
(síntesis en curso, actualizada sobre la marcha)

## Registro de preguntas y respuestas
### P1 - {tema}
- Pregunta: {pregunta}
- Registrado: {hechos y decisiones confirmados por el usuario, con sus palabras cuando importe}
- Tentativo / sugerido: {ideas no confirmadas, claramente marcadas}
- Pendientes: {asunto abierto -> responsable}
...

## Pendientes abiertos (esperan información)
- {asunto} -> {quién puede responder}
```

## Al terminar o al pausar

- **Revisa la captura** buscando contradicciones o vacíos. Marca explícitamente los conflictos sin resolver; no elijas un dato del negocio en nombre del usuario. Actualiza el estado de la sesión y el punto para retomarla.
- **Si la sesión era para construir o actualizar el contexto del AIOS:**
  - integra los hechos y preferencias duraderos confirmados por el usuario en la página de contexto existente que corresponda, con un enlace fechado a la captura, y conserva el contenido que no tenga relación;
  - registra las decisiones importantes confirmadas en el registro de decisiones existente, sin duplicar entradas;
  - lo desconocido, las ideas del brainstorm y las sugerencias del asistente quedan marcados en la captura hasta que se confirmen.
- **Si era una entrevista sobre un plan o un diseño y no pidieron actualizar el contexto canónico,** la captura original es el resultado. Sugiere `/conectar` para enrutar un resultado útil, o `/subir-nivel` para convertir una oportunidad elegida en una mejora. No ejecutes ninguno automáticamente.
- **Enrutamiento:** si el manual operativo o un índice existente todavía no dirige a `brainstorms/`, agrega esa ruta siguiendo las convenciones del proyecto y manteniendo la paridad del manual compartido.
  - Cada captura individual no necesita su propia entrada en el manual raíz.
  - Las capturas originales son evidencia fechada de una entrevista, no la verdad actual del negocio de forma automática.
- **Cierra con un resumen breve:**
  - la ruta clicable de la captura;
  - las páginas de contexto que realmente se actualizaron;
  - los pendientes que quedan;
  - el siguiente paso o punto para retomar.

## Límites y verificación

- **Alcance:** la captura local de la entrevista y las actualizaciones de contexto solicitadas. No edites la memoria global, no publiques, no envíes mensajes ni cambies sistemas externos. No pidas ni guardes credenciales; usa referencias o redacta los secretos.
- **Git:** el kit ignora `brainstorms/` en Git por defecto. Eso no quita las capturas que ya estén versionadas en un repositorio existente.
- **Casos a validar:** una sesión nueva, un choque de nombres en el mismo día, retomar una sesión, una respuesta que corrige otra, una solicitud de parar y un guardado fallido. Verifica que solo los hechos confirmados lleguen al contexto canónico y que las respuestas anteriores sigan siendo rastreables.
