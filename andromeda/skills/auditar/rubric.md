# Rúbrica de las Cuatro C, v2

Las Cuatro C (Four Cs) son Contexto (Context), Conexiones (Connections), Capacidades (Capabilities) y Cadencia (Cadence). Los IDs de criterio (C1…C5, N1…N5, P1…P5, D1…D5) se mantienen sin cambios para que los reportes sigan siendo comparables.

## Reglas de puntuación

Cada C tiene cinco criterios, y cada criterio vale 5 puntos.
- **Valores permitidos:** usa **solo 0, 1, 3 o 5**. Elige el nivel más alto que la evidencia respalde por completo.
- **Qué significa 0:** el criterio está ausente, contradicho o sin evidencia ni siquiera para el nivel de 1 punto.
- **Niveles acumulativos:** los niveles altos incluyen las comprobaciones sustantivas de los niveles inferiores. Las franjas de cobertura numérica (como en N1) son alternativas, no requisitos simultáneos.
- **Prohibido:**
  - interpolar;
  - empezar con el puntaje completo e ir restando;
  - dar puntos por infraestructura irrelevante;
  - reemplazar la evidencia faltante con optimismo.

**Evidencia y muestras:**
- En los niveles de varias partes, se requieren todas las partes.
- Una muestra acotada puede cumplir el criterio de muestra indicado, pero no prueba la cobertura de todo el sistema: nombra la muestra y el alcance sin resolver.
- Si no se pueden identificar flujos de trabajo o conexiones relevantes, los criterios que dependen de esa evidencia valen 0, no se consideran cumplidos por vacío.
- La documentación puede dar 1 punto donde se indica, pero no es un resultado que funcione.

## Contexto: ¿una sesión nueva puede entender y recuperar información? (25)

| ID | Criterio | 1 punto | 3 puntos | 5 puntos |
|---|---|---|---|---|
| C1 | Contexto operativo personalizado | Existen una identidad y un propósito que no son marcadores de plantilla | La identidad, la audiencia o las partes interesadas, las prioridades y las preferencias de colaboración tienen fuentes específicas y utilizables | Todo lo anterior es coherente en las fuentes actuales muestreadas, con prioridades significativas y expectativas de cierre claras |
| C2 | Enrutamiento y facilidad para encontrar | Un manual o equivalente da al menos una ruta específica y utilizable | Al menos 3 de las 5 pruebas funcionan por las rutas declaradas, y existen los índices importantes de proyectos o conocimiento donde hacen falta | Las 5 funcionan por las rutas declaradas; la comparación con las carpetas inmediatas no encuentra omisiones importantes sin explicar ni rutas muestreadas rotas |
| C3 | Vigencia | Los datos que cambian tienen fuente y fecha de corte | Los datos cambiantes muestreados tienen reglas de actualización adecuadas y evidencia actual, o están marcados explícitamente como históricos con una ruta funcional a la fuente actual | Todos los datos actuales muestreados están verificados dentro de su intervalo esperado; las cachés opcionales son coherentes, se mantienen y son opcionales, o no existen |
| C4 | Autoridad de las fuentes | Se identifica al menos una fuente canónica | Las reglas distinguen el contexto estable, el estado o las métricas actuales y los registros originales; las afirmaciones muestreadas enlazan a sus fuentes | Todas las cadenas de autoridad muestreadas se resuelven; los duplicados tienen roles explícitos y no quedan conflictos importantes sin resolver entre fuentes o manuales |
| C5 | Continuidad | Existe un registro real de una decisión o del estado de un proyecto | El proyecto activo muestreado tiene un entregable actual, el razonamiento de sus decisiones y un siguiente paso accesibles desde su punto de entrada | Un segundo proyecto o hilo de conocimiento relevante también se puede retomar desde registros durables, con estado actual y enlaces útiles a las fuentes |

No se exige una caché "caliente", una estructura de wiki específica, una carpeta de memoria, un manual largo ni una cantidad extra de proyectos. En una configuración que de verdad tiene un solo proyecto, el segundo hilo de C5 puede ser una decisión previa distinta dentro de ese proyecto.

## Conexiones: ¿puede alcanzar la información que necesita? (25)

Antes de puntuar, inventaría los dominios aplicables. Marca los dominios irrelevantes con una razón basada en el rol o el contexto del usuario. No premies conectar herramientas que el usuario no necesita.

| ID | Criterio | 1 punto | 3 puntos | 5 puntos |
|---|---|---|---|---|
| N1 | Acceso a los dominios relevantes | Al menos un dominio relevante tiene evidencia de lectura exitosa, pero menos de la mitad la tienen | Al menos la mitad de los dominios aplicables, pero no todos, tienen evidencia de lectura exitosa | Cada dominio aplicable tiene evidencia de lectura exitosa dentro de su intervalo esperado |
| N2 | Recuperación útil | Hay documentadas una consulta específica y su respuesta esperada | Una consulta real relacionada con una prioridad devuelve el registro, el rango de fechas y la fuente correctos | Dos consultas distintas relacionadas con prioridades devuelven resultados adecuados, y se revisaron la paginación y la completitud, o los límites de exportación documentados |
| N3 | Rutas de acceso reproducibles | Una conexión tiene documentados la ruta de la herramienta o el script y su propósito | Todos los dominios aplicables tienen una ruta documentada o un estado explícito de conexión faltante, y las rutas conectadas incluyen instrucciones de autenticación seguras y ejemplos de consulta | La ruta de acceso documentada muestreada se reproduce con éxito sin depender de contexto oculto del chat; todos los dominios conectados tienen guías utilizables |
| N4 | Límites de acción apropiados | Están documentados los permisos de lectura y escritura necesarios y los límites de aprobación | Para un flujo de escritura necesario, hay registrada una escritura previa autorizada y exitosa o un resultado fiel en un entorno de prueba; o bien está documentado y verificado que el usuario eligió un alcance de solo lectura | Las operaciones muestreadas respetan los permisos previstos y tienen protecciones verificadas contra fallas y duplicados; no hagas una escritura real solo para ganar puntos |
| N5 | Vigencia y visibilidad de fallas | Están documentadas las marcas de tiempo de las fuentes y las expectativas de vigencia | Las lecturas o exportaciones muestreadas cumplen esas expectativas, y las fallas se muestran en lugar de reemplazarse por datos viejos sin etiquetar | Cada dominio aplicable tiene evidencia reciente de éxito y, al menos en una conexión representativa, se demostró el manejo de autenticación vencida o datos desactualizados |

**Notas sobre las conexiones:**
- **N1 con un solo dominio:** si hay exactamente un dominio aplicable, su lectura exitosa cumple el nivel de cobertura de 5 puntos de N1; eso no cumple automáticamente los demás criterios.
- **Archivos locales y exportaciones:** pueden cubrir dominios relevantes cuando son la fuente real y están suficientemente al día.
- **Sin bonificaciones ocultas** por MCPs, claves de API, cantidad de proveedores ni permisos de escritura que el usuario no necesita.

## Capacidades: ¿los flujos de trabajo relevantes producen resultados utilizables? (25)

Usa hasta tres flujos de trabajo prioritarios, elegidos antes de inspeccionar sus resultados.
- Si solo existe uno, evalúalo con honestidad; no exijas skills innecesarios.
- Si una prioridad identificada necesita un flujo de trabajo que falta, mantén esa brecha en la muestra.

| ID | Criterio | 1 punto | 3 puntos | 5 puntos |
|---|---|---|---|---|
| P1 | Adecuación e invocación | Un flujo de trabajo tiene un disparador claro relacionado con una necesidad declarada | Un flujo muestreado tiene una invocación exitosa con las entradas previstas | Todos los flujos prioritarios muestreados tienen evidencia de invocación exitosa, con límites claros entre disparadores que se superponen |
| P2 | Calidad del resultado | Existen un resultado de ejemplo y criterios de aceptación | Un resultado real se revisó contra criterios de aceptación significativos | Todos los flujos muestreados tienen resultados utilizables verificados contra sus criterios de aceptación, no solo un "listo" autodeclarado |
| P3 | Manejo de fallas | Están documentados los casos esperados de entradas faltantes o errores, y los efectos secundarios | Se probó al menos un caso relevante de entrada faltante, fuente desactualizada o falla de dependencia, y se manejó correctamente | Cada flujo muestreado tiene un resultado de caso límite relevante y respeta los límites de autorización y de efectos secundarios |
| P4 | Portabilidad y descubrimiento | Están documentados los archivos y dependencias necesarios y la ruta de invocación | Los puntos de entrada, las referencias y los registros en el runtime muestreados se resuelven; donde se usan espejos generados, coinciden con las transformaciones requeridas | Una ejecución registrada en una sesión limpia (o un entorno aislado equivalente) reproduce el flujo muestreado sin estado oculto de la conversación ni dependencias no documentadas |
| P5 | Uso útil repetido | Hay evidencia de al menos un uso real fechado | Un flujo muestreado tiene dos usos reales exitosos y distintos, con referencias a sus resultados | Todos los flujos muestreados tienen usos reales exitosos repetidos; las correcciones se reflejan en el flujo actual y se validaron después |

La cantidad de skills o agentes y lo reciente de los archivos no dan puntos por sí solos. Un script determinista o un prompt simple puede puntuar tan alto como un agente complejo. Un skill recién creado no puede probar un uso real repetido ejecutando dos veces pruebas sintéticas.

## Cadencia: ¿el trabajo útil ocurre de forma confiable con el tiempo? (25)

Usa las programaciones reales y los momentos en que corresponde cada ejecución.
- Un ritual que se ejecuta a mano es útil, pero no es una ejecución desatendida.
- La configuración por sí sola no demuestra una ejecución exitosa.

| ID | Criterio | 1 punto | 3 puntos | 5 puntos |
|---|---|---|---|---|
| D1 | Disparador real | Existe un ritual humano explícito o una configuración real de programador o disparador | Al menos un disparador activado tiene un runtime o host verificado y un resultado esperado | Ese disparador se ejecutó de forma demostrable en su entorno desatendido previsto, incluidos los requisitos de disponibilidad del runtime |
| D2 | Ejecuciones a tiempo | Está registrada una finalización manual fechada o un intento automático incompleto o fallido | Una ejecución automática que correspondía se completó con su resultado esperado | Al menos dos ejecuciones automáticas distintas que correspondían se completaron; no quedan ejecuciones perdidas sin explicar en el período inspeccionado |
| D3 | Observabilidad | Están documentados el estado y el registro de las ejecuciones, y el comportamiento de notificación de fallas | Las ejecuciones inspeccionadas tienen marcas de tiempo y resultados durables, y una vía verificada para reportar fallas | Una falla real, o simulada de forma segura, llegó al mecanismo de reporte previsto, y hay evidencia de la recuperación |
| D4 | Control y recuperación | Existen instrucciones para detener o desactivar, responsables, permisos e instrucciones de recuperación | La configuración confirma esos controles y protege contra acciones duplicadas o superpuestas inapropiadas | Una prueba previa, o una prueba aislada y segura, demuestra la detención, la recuperación y la prevención de duplicados sin efectos secundarios no deseados |
| D5 | Ciclo de mantenimiento | Están definidos la frecuencia de revisión y los responsables de la vigencia y la limpieza | Una revisión completada reparó un problema real o verificó que no hacía falta actuar, con evidencia | Hay registrados dos ciclos de revisión programados distintos, con verificación posterior de cualquier arreglo y el enrutamiento y el contexto mantenidos |

**Durante una auditoría de solo lectura:**
- No dispares tareas, no cambies programaciones, no envíes alertas de prueba ni desactives automatizaciones. Usa evidencia previa o marca la prueba como no verificada.
- Un sistema solo manual tiene un máximo de **10/25 en Cadencia**, aunque su disciplina de revisión sea muy buena.
- Una rutina recién activada debe esperar evidencia de ejecuciones a tiempo: dos ejecuciones manuales de prueba seguidas no son dos ejecuciones que correspondían.

## Topes y etapas

1. Suma los puntos de los criterios de cada C. Si las cinco pruebas de recuperación no logran recuperar ni el propósito principal del usuario ni ninguna fuente autorizada de prioridades o estado, **Contexto tiene un tope de 10**. Muestra su subtotal bruto y el tope.
2. Aplica el tope de 10 en Cadencia para sistemas solo manuales cuando no se verifique ningún disparador automático activado. Esto incluye un sistema sin ningún disparador; el tope nunca suma puntos.
3. Suma los cuatro subtotales resultantes: ese es el **total bruto**.
4. Aplica todos los topes de total que correspondan; gana el más bajo:
   - Alguna C por debajo de 10: total con tope de **49**.
   - Alguna C por debajo de 15, o menos de dos ejecuciones automáticas exitosas verificadas: total con tope de **69**.
   - Alguna C por debajo de 20, o un conflicto importante sin resolver de enrutamiento o de autoridad de fuentes: total con tope de **84**.
5. Puntaje final = mín(total bruto, topes aplicables). Informa cada tope aplicado y por qué; nunca alteres la aritmética en silencio.

| Puntaje final | Etapa |
|---|---|
| 0-24 | Sin comprobar |
| 25-49 | Base |
| 50-69 | Funciona, con brechas |
| 70-84 | Confiable en el alcance verificado |
| 85-100 | Mantenido y con evidencia |

**Cómo presentar un puntaje alto:**
- Nunca lo presentes como universalmente autónomo, seguro o completo; indica qué se muestreó.
- La evidencia desconocida es una brecha de verificación, no una prueba de que el sistema esté roto.
- Estos topes impiden a propósito que una gran biblioteca de skills compense la falta de conexiones o de cadencia.

## Comprobaciones de calibración

- **Plantilla recién clonada:** con skills diarios con nombre, claves de API y marcas de tiempo recientes, no recibe puntos por ejecución, resultados ni acceso a dominios. Un clon nuevo debe quedar como "Sin comprobar", no saltar a 70 o más.
- **Mucha presencia, cero evidencia:** un manual personalizado, referencias útiles, 60 skills y 10 agentes, pero sin resultados ni ejecuciones observadas. La presencia no alcanza para el puntaje completo en Capacidades ni en Cadencia.
- **Cadencia solo manual:** Contexto, Conexiones y Capacidades excelentes con 25 cada una, y Cadencia solo manual con 10. Bruto 85, final 69: sin evidencia de éxitos automáticos aplica el tope de 69.
- **Sin conflictos:** todas las C en 21, con dos ejecuciones a tiempo exitosas y sin conflictos importantes, dan bruto y final de 84. Con 23 cada una en las mismas condiciones, bruto y final de 92.
- **Caché obligatoria desactualizada:** una caché "caliente" que contradice una fuente canónica baja los puntos de vigencia y autoridad, e impide un puntaje mayor a 84 hasta que se resuelva. No tener caché no se penaliza.
- **Rutinas nuevas frente a probadas:** una rutina mensual con dos ejecuciones a tiempo con evidencia puede recibir puntos por repetición; una tarea diaria recién configurada y sin ejecuciones, no.
