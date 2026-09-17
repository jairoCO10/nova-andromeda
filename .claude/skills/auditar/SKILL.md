---
name: auditar
description: Úsalo cuando alguien pida auditar su AIOS (también "audit"), puntuar las Cuatro C, encontrar rutas desactualizadas o proyectos sin enlazar, comparar AGENTS.md y CLAUDE.md, revisar la compatibilidad de skills entre Claude y Codex, o evaluar si está listo para migrar. Guarda automáticamente reportes fechados y da seguimiento, con evidencia, a las mejoras entre ejecuciones.
---

# Auditoría del AIOS

Comprueba si este AIOS puede encontrar la información correcta y hacer trabajo útil de forma confiable, e identifica cambios que le facilitarían el trabajo al usuario.

**Puntaje:**
- Puntúa **Contexto, Conexiones, Capacidades y Cadencia, sobre 25 cada una**, con [rubric.md](rubric.md). Esta es la rúbrica **v2**.
- Presenta el número como **confiabilidad operativa verificada**, no como utilidad general ni como porcentaje del trabajo que el AIOS puede hacer.
- Una carpeta, un skill instalado, una clave de API o una afirmación segura no prueban que el sistema funcione.

Habla con el usuario en español latinoamericano neutro, salvo que prefiera otro idioma.

**Cómo trabajar:**
- Trabaja localmente en el proyecto actual. No lances subagentes salvo que el usuario lo pida.
- Primero audita. `/conectar` repara una ruta y `/subir-nivel` ayuda a cerrar una brecha importante.
- Nunca infles ni bajes a propósito un puntaje para incentivar otra ejecución: la mejora viene de mejor evidencia y mejor comportamiento.

**Cada auditoría guarda automáticamente su reporte en la carpeta `audits/` del proyecto auditado.**
- Lee [history.md](history.md) para ver cómo elegir reportes previos, las transiciones de hallazgos, las reglas de comparación y el guardado seguro.
- Guardar el registro local de la auditoría es parte de este skill, no un paso de aprobación aparte.
- Una solicitud explícita del usuario de no guardar anula este comportamiento.
- El sistema inspeccionado no se modifica.

## 1. Define el alcance y la evidencia

- **Manuales:** obtén la fecha actual y la raíz del proyecto, y lee los `AGENTS.md`, `CLAUDE.md` y las anulaciones locales que correspondan, siguiendo la jerarquía de instrucciones del runtime.
  - Si existen ambos manuales, léelos los dos.
  - Busca enrutamientos en conflicto y sincronizaciones prometidas, sin suponer que las instrucciones distintas de cada runtime deban ser idénticas.
- **Historial:** carga el reporte previo del AIOS que corresponda y el registro de hallazgos arrastrado, usando [history.md](history.md), antes de elegir las pruebas.
  - Vuelve a revisar los hallazgos previos importantes junto con las prioridades actuales; no supongas que los resultados anteriores siguen siendo ciertos.
  - Identifica la línea base de comparación y los cambios de alcance antes de puntuar.
- **Qué leer y qué omitir:**
  - Aplica primero las reglas de enrutamiento del manual.
  - Lee sus índices de proyectos y de conocimiento antes de listar sus carpetas inmediatas.
  - Inspecciona solo los manuales con alcance que sean relevantes.
  - Omite dependencias, cachés, resultados generados y archivos archivados, salvo que una ruta apunte ahí o haga falta aclarar una ambigüedad entre lo archivado y lo actual.
- **Perfil del usuario:** identifica su rol, su objetivo principal, sus prioridades actuales y hasta tres flujos de trabajo importantes, a partir del contexto real.
  - Los marcadores de plantilla sin completar no cuentan.
  - No exijas datos de ingresos del negocio a alguien cuyo trabajo no tiene una función de ingresos.
- **Infraestructura:** inspecciona los registros de skills y agentes compatibles, las referencias de conexiones, y la configuración real del programador de tareas con su evidencia de ejecución.
  - Acepta por igual scripts, MCPs, exportaciones, datos locales y mecanismos equivalentes.
  - Los inventarios sirven solo para orientarte.
- **Registro de hallazgos:** marca cada uno como **verificado**, **documentado pero sin verificar**, **faltante**, **desactualizado** o **en conflicto**, con referencia de archivo y línea, URL de la fuente o una ejecución fechada.
  - Las fechas de modificación de los archivos y las etiquetas de "última revisión" no prueban por sí solas que haya habido una actualización o ejecución exitosa.
- **Tiempo y cobertura:** empieza con lecturas específicas.
  - Si un límite de tiempo o de páginas impide verificar algo, márcalo como sin verificar e indica la cobertura.
  - Nunca des puntaje completo porque no hubo tiempo de revisar.
  - No declares una auditoría exhaustiva a partir de una muestra.

## 2. Prueba el enrutamiento y la recuperación de contexto

Haz un mapa compacto: **necesidad del usuario → manual/índice → fuente específica → regla de vigencia**.
- Incluye, según corresponda:
  - el contexto del negocio, las personas y las prioridades o compromisos;
  - los registros originales y los entregables de proyectos;
  - las bases de conocimiento especializadas, los medios y assets, y los sistemas externos.
- Un nombre genérico de carpeta o de proveedor no alcanza si deja sin claro cuál es la fuente relevante.

Compara el mapa con las carpetas inmediatas para encontrar:
- proyectos importantes sin índice;
- conteos desactualizados y rutas rotas;
- alias ambiguos y fuentes de verdad duplicadas;
- material retirado presentado como activo.

Distingue las brechas confirmadas de las carpetas cuya relevancia se desconoce. Revisa si las rutas indicadas funcionan desde la copia actual, incluidas las referencias dentro de los skills y de los espejos generados donde ese runtime los use.

Sigue las rutas declaradas para estas cinco preguntas, adaptadas al trabajo real del usuario:

1. ¿Qué hace esta persona o negocio, para quién y qué importa ahora?
2. ¿Dónde está la prioridad, el compromiso o el estado actual autorizado, y cómo lo verificaría?
3. ¿Dónde está el último entregable y el siguiente paso de un proyecto activo importante?
4. ¿Dónde está una decisión previa, una lección o un conocimiento específico, y su fuente de respaldo?
5. ¿Dónde está un registro externo, asset o documento original que se necesite con frecuencia, y cómo se accede?

**Cómo aplicar las pruebas:**
- **Antes de buscar:** elige ejemplos relevantes antes de buscar las respuestas. Si una categoría no aplica, registra por qué y reemplázala por otra necesidad de recuperación real, manteniendo cinco pruebas.
- **Qué mostrar en cada una:**
  - la pregunta y la ruta intentada;
  - la fuente y el resultado;
  - si se encontró directamente, solo con una búsqueda alternativa o no se encontró.
- **Qué cuenta como evidencia:**
  - Una búsqueda amplia puede recuperar la respuesta, pero no prueba que la ruta declarada funcione.
  - Si no revisaste un acceso externo, márcalo como sin verificar; una ruta de acceso documentada recibe solo el puntaje de documentación.
  - Puntúa solo la evidencia que realmente observaste.

**Revisa explícitamente la vigencia y la autoridad:**

- **Cachés y resúmenes:** un `_hot.md`, un resumen o una caché opcional no suma puntos solo por existir, y no recomiendes crear uno por defecto.
  - Revisa si duplica páginas canónicas, si tiene un mecanismo real de actualización y si presenta como actuales cifras viejas o plazos vencidos.
  - Un encabezado editado hace poco no actualiza todos los datos que contiene.
- **Caché sin mantenimiento:** si agrega duplicación sin un mantenimiento confiable, recomienda saltarla en la recuperación y usar directamente el índice o la fuente relevante.
  - Nunca la elimines automáticamente.
  - No tener caché es una arquitectura válida.
- **Dónde vive cada tipo de dato:**
  - El contexto estable puede vivir en una wiki.
  - Las métricas actuales y el estado de las tareas deben resolverse en el sistema vivo correspondiente o en una exportación fechada.
  - Los términos exactos deben resolverse en los registros originales.
  - Revisa las fechas de las fuentes y marca los conflictos, en lugar de tratar la wiki como autoridad automática para cualquier tipo de dato.
- **Sesión nueva:** revisa si podría entender al usuario, retomar el proyecto seleccionado y encontrar evidencia sin depender de esta conversación.
  - Valora un enrutamiento compacto y preciso.
  - No premies la longitud del manual, los catálogos exhaustivos en la raíz ni que haya que leer todas las páginas de la wiki.

## 3. Verifica las otras tres C

**Compatibilidad primero:** ejecuta las [comprobaciones obligatorias de enrutamiento y compatibilidad entre runtimes](compatibility.md). Cubren:
- rutas desactualizadas o rotas;
- trabajo importante sin enlazar;
- diferencias entre manuales operativos;
- disponibilidad de skills en los runtimes que se usan o que se quieren migrar.

Compara el comportamiento compartido y los recursos necesarios, no solo la igualdad literal de los archivos. Registra por separado las diferencias esperadas entre runtimes y los defectos. El protocolo también define la tabla de compatibilidad obligatoria, las etiquetas de evidencia y los casos de calibración.

**Conexiones:** identifica los dominios aplicables:
- finanzas e interacciones con clientes;
- calendario y comunicación;
- tareas, reuniones y conocimiento o archivos;
- dominios de contenido o especializados, si son relevantes.

Registra de cada dominio su relevancia, su mecanismo, la ruta de acceso específica, la evidencia de lectura exitosa, la fecha y las limitaciones.
- **Una herramienta, varios dominios:** solo si cada dominio tiene su evidencia.
- **Autenticación:** un MCP configurado o una clave en `.env` no demuestran que esté autenticada.
- **Cómo comprobar:** usa comprobaciones de solo lectura acotadas y seguras cuando existan, o evidencia fechada de ejecuciones exitosas dentro del intervalo de actualización esperado de la fuente.
  - Si no hay un intervalo documentado, usa 30 días y explica por qué los datos muy cambiantes pueden requerir una lectura nueva.
- **Seguridad:**
  - No imprimas valores secretos ni registros privados en bloque.
  - No ejecutes scripts desconocidos antes de revisar sus efectos secundarios.

**Capacidades:** elige hasta tres flujos de trabajo relacionados con las prioridades identificadas, no solo las demos más pulidas.
- **Qué examinar:**
  - disparadores, entradas y destino del resultado;
  - ejemplos de resultados realmente utilizables;
  - verificación, manejo de fallas y uso repetido.
- **Brechas y estructura:**
  - Los flujos faltantes siguen siendo brechas.
  - Revisa si se pueden descubrir, si tienen los archivos de apoyo necesarios y si la copia canónica y el espejo coinciden después de las transformaciones documentadas.
- **Sin bonificaciones:** los agentes son opcionales; la cantidad, la complejidad y los nombres personalizados no dan puntos extra.
- **Cómo comprobar:** usa resultados existentes o comprobaciones acotadas y seguras. No inicies una generación pagada ni trabajo sustancial solo para auditarlo.

**Cadencia:** inspecciona las programaciones realmente activadas, los disparadores por eventos, los hooks o los rituales humanos definidos explícitamente, junto con sus registros de ejecución.
- **Qué identificar:**
  - el host o runtime y el disparador;
  - el resultado esperado y la última ejecución que correspondía;
  - la evidencia de éxito o falla;
  - los controles para detener y recuperar.
- **Qué no cuenta:** un skill llamado `daily-*`, una plantilla o archivos editados hace poco no demuestran una cadencia.
- **Rituales manuales:** un ritual manual útil recibe un puntaje limitado; márcalo como manual.
- **Tareas locales:** no llames desatendida ni independiente de la laptop a una tarea local sin evidencia en ese entorno.
- **Rutinas mensuales o trimestrales:** evalúalas según sus fechas reales, no con una ventana semanal fija.

## 4. Puntúa y prioriza

**Cómo calcular:**
- Lee completa la [rúbrica](rubric.md).
- Asigna los 20 puntajes de criterio y después aplica sus topes.
- Muestra los cuatro subtotales, la suma bruta, cualquier tope y su razón, el puntaje final y la etapa.
- La evidencia faltante no da puntaje verificado, pero distingue **sin verificar** de **roto confirmado**.
- Registra los dominios excluidos con sus razones; no excluyas un dominio solo porque está desconectado.

**Cómo priorizar:**
- Ordena las brechas por su efecto probable en el trabajo del usuario: las respuestas incorrectas o desactualizadas y la falta de acceso a fuentes van antes que el orden cosmético.
- Da hasta tres arreglos concretos, cada uno con:
  - la ruta o el flujo afectado exacto;
  - la evidencia que lo respalda;
  - una comprobación de cierre clara.
- No inventes tres fallas en un sistema sano.
- Distingue una reparación de una comprobación necesaria para resolver una incertidumbre.

**Cómo agrupar los hallazgos:**
- Agrúpalos en **defectos confirmados**, **brechas de verificación** y **oportunidades de mejora**, y lista aparte las diferencias intencionales.
- Mantén separadas la gravedad y la confianza.
- Asigna a cada problema de fondo un ID estable y reutilízalo en todas las secciones. No cuentes un mismo espejo faltante o una misma ruta mala como varios defectos independientes.
- Indica qué criterios de la rúbrica existente afecta. No introduzcas un puntaje de migración ni cambies los niveles de la v2.

**Cómo explicar los límites:**
- Explica las limitaciones del puntaje, incluidos los límites por cadencia manual cuando correspondan.
- La evidencia no revisada no prueba una falla.
- Las mejoras opcionales no son defectos solo porque no están.

## 5. Entrega un reporte conciso y revisable

Usa esta estructura y mantén compacto el registro de evidencia:

1. **Auditoría del AIOS: fecha, proyecto, rúbrica v2.**
   - Incluye el alcance, los runtimes, los límites de verificación y una conclusión en lenguaje simple.
   - Empieza por lo que funciona y la diferencia más importante.
   - Informa los conteos de hallazgos únicos por clase, no como un total exhaustivo fuera del alcance inspeccionado.
2. **Hallazgos de AGENTS.md / CLAUDE.md:** incluye siempre la sección dedicada que se describe abajo, aunque no haya problemas. No escondas los hallazgos del manual operativo entre los arreglos generales o en la tabla de enrutamiento.
3. **Enrutamiento y compatibilidad de migración:**
   - Muestra la cobertura o matriz y los hallazgos accionables de [compatibility.md](compatibility.md): defectos confirmados, brechas de verificación, diferencias intencionales y oportunidades de mejora.
   - Referencia los IDs existentes en lugar de repetir los hallazgos completos del manual.
   - Indica si la migración muestreada está bloqueada, necesita verificación o aprobó las comprobaciones inspeccionadas. No des a entender que todo el sistema es portable a partir de una muestra.
4. **Prueba de enrutamiento:** los resultados de las cinco pruebas, con las referencias de las fuentes y el estado (directo / búsqueda alternativa / sin resolver).
5. **Qué funciona:** hasta tres fortalezas respaldadas con evidencia.
6. **Confiabilidad operativa verificada:**
   - Cuatro filas, cada una `/25`, con el total bruto, los topes, el final `/100` y la etapa.
   - Incluye los IDs de criterio y los puntos asignados para que la aritmética sea reproducible.
   - Explica por separado cómo limitaron el puntaje los defectos confirmados y la evidencia sin verificar.
   - No es una calificación de utilidad general.
7. **Mejoras principales:** hasta tres acciones ordenadas, cada una:
   - marcada como reparar, verificar o mejora opcional;
   - con evidencia, la siguiente acción exacta, el beneficio práctico esperado y qué probaría que está completa.

   Referencia los IDs en lugar de repetirlos completos.
8. **Avance desde la auditoría anterior:**
   - Enlaza la línea base y muestra las transiciones de hallazgos y la evidencia de [history.md](history.md).
   - Explica cualquier cambio comparable de puntaje, separando las reparaciones reales, la evidencia recién verificada, las regresiones y los cambios de cobertura o de rúbrica.
   - Si no hay un reporte previo comparable, es una línea base nueva, no una mejora inventada.
9. **Próxima ejecución:**
   - Da un prompt listo para usar con `/subir-nivel` que lleve la brecha de mayor valor, su evidencia y su comprobación de aceptación. Para un arreglo solo de enrutamiento, usa `/conectar <destino> <propósito>`.
   - Recomienda estos comandos solo si están instalados; si no, da la tarea equivalente en lenguaje simple.
   - `/entrevistame`, si está disponible, sirve para contexto que de verdad falta, no para datos que ya están guardados en otro lugar.
10. **Registro guardado:**
    - Escribe y relee el reporte completo con [templates/report.md](templates/report.md), y enlaza el archivo realmente guardado en la respuesta final.
    - El chat puede ser conciso; el registro guardado debe conservar el desglose del puntaje, la evidencia, las comprobaciones de compatibilidad y el registro de hallazgos arrastrado.
    - Nunca digas que se guardó sin confirmarlo.

### Sección obligatoria: hallazgos de AGENTS.md / CLAUDE.md

**Qué declarar primero:**
- Nombra los manuales raíz exactos que inspeccionaste y los manuales con alcance que muestreaste.
- Marca cada manual raíz como **revisado**, **faltante** o **no revisado**, con la razón cuando haga falta.
- Indica si su guía compartida coincide, entra en conflicto o difiere de forma intencional.
- No des a entender que inspeccionar un archivo verifica el otro. Una configuración con un solo manual aplicable no necesita un duplicado para aprobar.

Después muestra una tabla compacta de hallazgos:

| Archivo y sección/línea | Regla o ruta faltante | Hallazgo y efecto práctico | Cambio recomendado |
|---|---|---|---|
| Referencia de archivo exacta y clicable | Cita corta o paráfrasis precisa; marca las omisiones explícitamente | Qué se verificó, qué está desactualizado, en conflicto, roto o sin verificar, y cómo afecta encontrar o usar la información | Edición específica o paso de verificación |

**Cómo completar la tabla:**
- **Manual frente a archivos enrutados:** separa los **problemas del propio manual** de los **problemas en los archivos a los que dirige**.
  - Por ejemplo, un índice de destino desactualizado es una brecha de mantenimiento aguas abajo, salvo que el manual también dirija al índice equivocado.
  - Nombra el archivo aguas abajo y la ruta que llega a él.
- **Fortalezas:** incluye una frase breve sobre lo que los manuales ya hacen bien.
- **Sin problemas:** di explícitamente "No se encontraron problemas en los manuales operativos dentro del alcance inspeccionado" e indica los límites de cobertura. No inventes hallazgos para llenar la tabla.

**Cómo cerrar la sección:**
- Indica si se modificó algún manual. En una auditoría estándar de solo lectura, di **"No se modificó ningún manual operativo."**
- Estos hallazgos alimentan los criterios y topes existentes de las Cuatro C: no agregues un quinto puntaje ni restes dos veces por lo mismo.
- Aplica esta sección tanto en los reportes del chat como en los guardados.

**Cuándo volver a auditar:**
- Recomienda volver a ejecutar `/auditar` después del arreglo seleccionado, cada semana durante la configuración activa y después con un intervalo de mantenimiento razonable.
- Compara con un reporte guardado anterior solo si coinciden el alcance y la rúbrica; los puntajes de la v1 necesitan una línea base nueva.
- Los puntajes pueden bajar cuando la evidencia se desactualiza. No prometas un puntaje mayor solo por volver a ejecutar.

**La auditoría es de solo lectura para los sistemas inspeccionados:**
- Nada de reparaciones, movimientos de archivos, instalaciones, cambios en programaciones, mensajes ni escrituras externas.
- Su única escritura por defecto es un reporte local nuevo en `audits/` (crea la carpeta si hace falta).
- Conserva los reportes anteriores y redacta los secretos y los registros privados innecesarios.
- No actualices la memoria del negocio ni los archivos de fuente de verdad a partir de las observaciones de la auditoría.
- **Si la ejecución queda incompleta:** guarda, cuando sea posible, un reporte parcial claramente marcado. No lo presentes como una auditoría completa ni inventes un puntaje.
- **Si falla el guardado:** dilo explícitamente y entrega el reporte en el chat.
