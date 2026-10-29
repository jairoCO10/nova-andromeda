---
name: subir-nivel
description: Úsalo cuando alguien pida subir de nivel su AIOS, cerrar una brecha de la auditoría, encontrar qué automatizar después o mejorar un flujo de trabajo (también "level up"). Recorre las 3 M (Mentalidad, Método, Máquina), desde elegir la restricción hasta entregar un artefacto útil o una reparación verificada.
---

> *Adaptado de The Three Ms of AI™. © 2026 Nate Herk. Todos los derechos reservados.*
> *The Three Ms of AI™ es una marca registrada de Nate Herk.*
> *En esta traducción, "las 3 M" = Mentalidad (Mindset), Método (Method) y Máquina (Machine).*

## Qué hace este skill

Guía al usuario por las 3 M cada semana para encontrar y entregar una automatización nueva. **Una entrevista = un artefacto.** Además, con el tiempo instala el marco de las 3 M en la cabeza del usuario: después de 4 a 6 ejecuciones, el usuario empieza a detectar oportunidades a mitad de semana sin que nadie se lo pida, porque las preguntas ya se volvieron su forma natural de pensar.

Este es el mecanismo para reentrenar el cerebro. El kit no necesita tareas programadas para anclar el hábito; necesita que `/subir-nivel` se ejecute todos los viernes.

Habla con el usuario en español latinoamericano neutro, salvo que prefiera otro idioma. Los nombres de los principios del framework (Default Shift, Lego Principle, Bike Method, etc.) pueden citarse en inglés, con su explicación en español.

## Qué NO es `/subir-nivel`

- No es `/auditar`. `/auditar` es estructural ("¿el AIOS está bien construido?"). `/subir-nivel` es funcional ("¿qué palanca de negocio estoy desaprovechando?"). Si la estructura está desordenada, ejecuta primero `/auditar`.
- No es un planificador de varias opciones a la vez: una ejecución = un artefacto entregado.
- No es un coach. El usuario piensa; el skill conduce la entrevista.

## Cuándo se ejecuta `/subir-nivel`

- **Primera ejecución: Día 14.** Después de que el usuario conectó al menos un MCP o script y ejecutó `/auditar` una vez. Antes de eso, el resultado es trivial.
- **Frecuencia: semanal, el viernes por la tarde.** Revisa la semana, encuentra una automatización y entrégala el lunes.
- **A pedido, en cualquier momento.** A mitad de semana, si una tarea manual está molestando.

## Qué lee el skill

Primero lee el manual operativo que corresponda. Las rutas de abajo son las del kit base: si el proyecto usa otras ubicaciones, busca las prioridades, la identidad y las conexiones en sus rutas declaradas. No crees archivos de contexto duplicados solo porque falten estas rutas por defecto. Usa `references/3ms-framework.md` si existe; si no, lee el [framework de las 3 M](references/3ms-framework.md) incluido. Pregunta solo por la información que no esté en las fuentes existentes.

- `context/priorities.md`: lo que el usuario dijo que importa.
- `context/about-me.md`: `top_pain` y rol.
- `connections.md`: qué se puede alcanzar y con qué mecanismo.
- `references/3ms-framework.md`: el framework (para citar sus principios).
- `decisions/log.md`: decisiones recientes (qué ya se entregó o se consideró).
- El frontmatter de `.agents/skills/*/SKILL.md`: qué capacidades existen.
- Los `audits/audit-{fecha}.md` recientes, si existen.

## Ejecución: tres fases

### Si vienes de una auditoría

Si el usuario trae un hallazgo de `/auditar`, o hay un reporte reciente, lleva a la Fase 1:
- su evidencia;
- la ruta o el flujo de trabajo afectado;
- la comprobación de cierre.

Usa esa brecha como primera candidata y pregunta solo por el contexto que falte, en lugar de reiniciar una entrevista genérica. No persigas puntos ni supongas que una conexión sin verificar está rota.

**Qué hacer según el tipo de brecha:**
- **Arreglo solo de enrutamiento:** usa `/conectar` si está disponible y el usuario pidió la edición.
- **Reparación de un flujo de trabajo seleccionado:** mejora ese flujo existente en lugar de crear un skill duplicado. Una reparación verificada cuenta como el artefacto de esta ejecución.
  - Conserva el razonamiento del Método, el alcance y los permisos relevantes, y los pasos de validación.
  - Una medida práctica puede ser: menos recuperaciones fallidas, menos ejecuciones perdidas o menos tiempo buscando una fuente.
  - En las reparaciones, omite la estructura que solo aplica a creaciones: los encabezados de la Fase 3 son para artefactos de flujo de trabajo nuevos, nunca para manuales operativos ni índices de enrutamiento.

Cierra con la evidencia de aceptación de la reparación y recomienda volver a ejecutar `/auditar`. No declares un puntaje mayor hasta que la nueva auditoría lo verifique; la evidencia de uso repetido y de ejecuciones a tiempo se acumula solo con el uso real.

### Fase 1: Entrevista de Mentalidad (encontrar la candidata)

Encuentra de 1 a 3 candidatas, ordenadas por palanca. Haz estas preguntas en orden, de forma conversacional:

1. *"Cuéntame tu semana. ¿Qué hiciste 3 veces o más?"* (frecuencia)
2. *"¿Algo se sintió manual, aburrido o de copiar y pegar?"* (trabajo pesado)
3. *"¿En qué pensaste 'esto lo podría hacer un practicante listo'?"* (delegación)
4. *"Si mañana llegaran 500 clientes nuevos, ¿qué se rompería primero?"* (restricción)
5. *"¿Qué te daría 500 clientes más mañana?"* (palanca de crecimiento)

Cita los principios de Mentalidad cuando encajen:
- *"Parece que aplica el Default Shift: ¿hasta qué punto se podría aprovechar la IA aquí?"*
- *"Esto es el Function Breakdown: no vas a automatizar todo el trabajo, solo esta parte."*
- *"La IA es mejor de lo que crees y mejora más rápido de lo que crees. Si el trimestre pasado no podía hacer esto, quizá ahora sí."*

**Resultado de la Fase 1:** una lista numerada de 1 a 3 oportunidades, con una línea por candidata sobre "por qué esto es palanca". Pregunta: *"Elige una para definirla."*

### Fase 2: Entrevista de Método (definir una)

El usuario elige una candidata. Recorre los 5 pasos del Método:

**Paso 1: Encuentra la restricción.** ¿Qué cuello de botella resuelve o qué palanca de crecimiento abre? Relaciónalo con las respuestas de la Fase 1.

**Paso 2: EAD, es decir, Eliminar / Automatizar / Delegar.**
- **Primero, eliminar:** *"¿Qué pasa si simplemente dejamos de hacer esto?"* Si la respuesta es "no se rompe nada", el skill termina con buen ánimo: *"No automatices el desperdicio."* Es un logro: regístralo en `decisions/log.md` y detente.
- **Segundo, automatizar:** aplica la proporción 60/30/10: ~60 % determinista, ~30 % asistido por IA y ~10 % manual.
- **Tercero, delegar:** si es demasiado complejo, variable o depende mucho del criterio, sugiere a una persona. El skill termina con una sugerencia de delegación y la registra.

**Paso 3: Mapea el proceso.** Cinco elementos:
- Disparador (qué lo inicia)
- Fuentes de datos (de dónde viene la información)
- Transformaciones de datos (cómo cambia la forma de los datos)
- Puntos de decisión (dónde se ramifica)
- Destino (a dónde va el resultado)

Si el usuario no puede explicar alguno de los cinco: *"Si no se lo puedes explicar a una persona, no se lo puedes explicar a una IA. Dibújalo primero en papel y después vuelve."* El skill se detiene.

**Paso 4: Elige el nivel de autonomía.**

| Nivel | Nombre | Qué pasa |
|---|---|---|
| L0 | Manual | Sin IA |
| L1 | Sugerido | La IA sugiere; una persona decide cada paso |
| L2 | Borrador | La IA redacta; una persona revisa y edita |
| L3 | Supervisado | La IA ejecuta; una persona valida periódicamente |
| L4 | Autónomo | La IA se encarga de principio a fin |

**Por defecto = el nivel más bajo que resuelva el problema.** Cuestiona el L4, salvo que el usuario ya haya pasado explícitamente por los niveles inferiores. *"Los flujos de trabajo le ganan a los agentes. Si una decisión no TIENE que tomarla una IA, no dejes que la tome."*

**Paso 5: Relaciónalo con un KPI.** ¿Qué categoría de los Tres Baldes (Three Buckets) mueve?
- Más clientes
- Más valor por cliente
- Menos costo

Y una métrica específica (tiempo de respuesta, tasa de error, tasa de conversión, tiempo hasta completar). **Si el usuario no puede nombrar una categoría y una métrica, el skill se detiene.** *"Si tu automatización no mueve un número, ¿para qué la estás construyendo?"*

**Resultado de la Fase 2:** la especificación de la automatización, escrita en `decisions/log.md` como una entrada fechada con las cinco respuestas, el nivel de autonomía y el KPI. Es el registro durable de qué se decidió y por qué.

### Fase 3: Entrega a la Máquina (construirlo)

Pregunta: *"¿Cómo quieres entregar esto?"*. Las opciones van ordenadas según el principio Boring-is-Beautiful ("lo aburrido es bello"):

1. **Solo prompt:** una plantilla de prompt guardada que el usuario ejecuta a mano. Cero infraestructura; la mayor participación manual.
2. **Skill determinista:** un SKILL.md que ejecuta un script (sin paso de IA). Ideal para transformaciones con reglas claras.
3. **Skill asistido por IA:** un SKILL.md con una llamada a la IA adentro. Redacta, clasifica o resume.
4. **Subagente:** un agente de varios pasos. Último recurso: solo si el trabajo de verdad necesita razonamiento y uso de herramientas.

**Opción por defecto = la opción sin IA más alta que resuelva el problema.** El usuario tiene que elegir explícitamente más autonomía.

Una vez elegida, usa el generador que corresponda:
- `skill-creator`, si está disponible de forma global (lo distribuye Anthropic);
- `skill-builder`, si el usuario lo tiene localmente;
- si no, escribe directamente un SKILL.md o archivo de agente con su frontmatter, su ubicación y su contenido. Nombra los skills nuevos en español, en minúsculas, sin tildes y con guiones.

**Cada artefacto generado lleva estos dos encabezados al inicio** (las claves se mantienen en inglés por compatibilidad):

```markdown
---
bike-method-phase: 1  # Fase 1: rueditas de entrenamiento. Ejecútalo primero a mano.
three-ms-attribution: |
  Adaptado de The Three Ms of AI™ © 2026 Nate Herk.
---
```

Esto deja al usuario en la Fase 1 del Bike Method en la primera construcción, para que no se salte la validación manual sin darse cuenta. La fase solo avanza con una edición explícita.

Menciona los principios de Máquina al generar el artefacto:
- **Lego Principle:** los pasos más pequeños posibles; si se puede, primero sin IA.
- **Validation Chain:** prueba cada paso antes de encadenarlo.
- **Iteration Mindset:** entrega la prueba de concepto y amplíala según el uso real.

## Contrato de resultado

Cada ejecución de `/subir-nivel` produce:

1. **Una entrada en `decisions/log.md`**, fechada, con la especificación del Método.
2. **Una mejora entregada:** un prompt, un skill o un archivo de agente, o una reparación verificada del flujo de trabajo o del enrutamiento seleccionado.
3. **Un cierre de una pantalla:** qué se definió, qué se construyó y el recordatorio de la Fase 1 del Bike Method.

## Reglas críticas de implementación

1. **Una entrevista = un artefacto.** Nada de definir varias candidatas en paralelo.
2. **La fase de Mentalidad siempre va primero.** Aunque el usuario llegue con una idea ya formada.
3. **El EAD obliga a "eliminar primero".** Si la respuesta es Eliminar, termina con buen ánimo: es un logro, no un fracaso.
4. **Por defecto, el nivel de autonomía más bajo que funcione.** Cuestiona el L4.
5. **Boring-is-Beautiful por defecto en la entrega a la Máquina.** Por defecto, la opción sin IA más alta.
6. **Relacionarlo con un KPI es obligatorio.** Si el usuario no puede nombrar categoría y métrica, el skill se detiene.
7. **El Bike Method va en cada artefacto.** `bike-method-phase: 1` en el frontmatter.
8. **Limita las ediciones a `decisions/log.md` y al artefacto seleccionado.** Una reparación de auditoría seleccionada explícitamente puede actualizar su flujo de trabajo o sus archivos de enrutamiento existentes; conserva el contenido que no tenga relación. Los demás archivos son de solo lectura.
9. **Marca registrada y atribución en el resultado.** Cada reporte y cada artefacto generado hacen referencia al framework.

## Verificación (para quien implementa)

- **Prueba en seco** en un AIOS con contexto real, sin prompt. En el original se probó con el AIOS Herk-2 de Nate Herk. Resultado esperado: el skill propone 2 o 3 candidatas tomadas de la actividad reciente, las prioridades y el `top_pain`. Un resultado genérico ("deberías crear un resumen") = falla.
- **Prueba de "eliminar primero":** da una candidata que obviamente se puede eliminar. Resultado esperado: el skill sugiere Eliminar, termina y registra el logro.
- **Prueba de freno al L4:** el usuario pide en la primera construcción un agente que responda correos de forma autónoma. Resultado esperado: el skill insiste en empezar por L1/L2 y no entrega un L4 sin una anulación explícita.
- **Prueba de Boring-is-Beautiful:** una candidata que se resuelve con Python determinista. Resultado esperado: el skill recomienda por defecto `(2) skill determinista`.
- **Prueba contra saltarse el Bike Method:** el usuario genera un artefacto y pide pasar de inmediato a la Fase 4. Resultado esperado: el skill le hace leer qué significa cada fase y confirmar que validó las fases anteriores.

---

> *The Three Ms of AI™ es una marca registrada de Nate Herk. © 2026 Nate Herk. Todos los derechos reservados.*
