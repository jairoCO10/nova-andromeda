# Historial automático de auditorías

Lee este archivo al inicio de cada auditoría del AIOS. Los reportes fechados son el historial durable, y cada reporte nuevo arrastra el registro de hallazgos. No mantengas una base de puntajes editable aparte ni dependas de esta conversación. Escribir reportes no programa auditorías futuras ni repara el sistema inspeccionado.

**Compatibilidad con reportes anteriores:** las claves y los valores del frontmatter YAML (`audit_kind: aios`, `report_status: complete` / `partial`, `rubric_version: v2`, etc.) se mantienen en inglés porque son datos. Los reportes generados antes de la traducción pueden tener encabezados y estados en inglés; usa la tabla de equivalencias de la sección 2 para interpretarlos.

## 1. Selecciona la evidencia previa

1. **Ubica la raíz del proyecto auditado y su carpeta `audits/` existente.** Revisa primero los nombres y metadatos de los reportes, no el contenido completo de cada auditoría. La carpeta también puede contener auditorías de costos, de código o de seguridad: esas no sirven como línea base del AIOS.
2. **Elige los reportes** según `audit_kind: aios`, la identidad del proyecto, la marca de tiempo de la ejecución, el estado del reporte, la versión de la rúbrica y la cobertura.
   - Si un reporte antiguo no tiene metadatos, lee sus encabezados y su alcance, e identifícalo explícitamente como antiguo. Nunca adivines puntajes, IDs ni fechas de memoria.
   - No modifiques archivos históricos para ajustarlos al formato nuevo.
3. **Lee los reportes base.**
   - Lee el registro del último reporte aplicable y, si es distinto, el del reporte completo y comparable más reciente. Empieza con dos reportes completos como máximo.
   - Sigue enlaces más antiguos solo si hay una identidad o evidencia sin resolver, o un alcance comparable más antiguo. Si no es posible, anota la limitación.
   - Excluye los reportes de fixtures o de ejemplo.
   - Si hay ejecuciones superpuestas o paralelas, revísalas para que los hallazgos sin resolver de una rama no desaparezcan.
4. **Compara puntajes solo** en el mismo proyecto, con la misma rúbrica y un alcance materialmente equivalente: runtimes, dominios, flujos de trabajo y pruebas de recuperación.
   - Una copia movida del mismo proyecto puede calificar si se verifica su identidad.
   - Los proyectos distintos, los criterios de puntuación modificados, las muestras más estrechas o más amplias y los reportes parciales no permiten una diferencia simple de puntaje.
   - Las comparaciones a nivel de hallazgo pueden seguir siendo válidas cuando los destinos y las comprobaciones coinciden.
5. **Registra el enlace a los reportes previos y, por separado, la línea base de puntaje,** si existe.
   - Si no hay un reporte guardado elegible, es la **primera línea base registrada**.
   - No trates una auditoría no guardada como evidencia recién verificada.
   - Importar historial requiere una solicitud explícita, con la fuente y la fecha claramente indicadas.

## 2. Mantén la identidad y el estado de los hallazgos

Da a cada hallazgo de fondo nuevo un ID estable, como `AIOS-<run-id>-01`.
- **ID original:** consérvalo en las ejecuciones siguientes. Para reconocer el mismo hallazgo, compara la ruta o el flujo afectado, el runtime y el modo de falla.
- **Renombres y movimientos:** registra los verificados en lugar de crear hallazgos duplicados.
- **Identidad ambigua:** explícala antes de fusionar.
- **Campos separados:** la clase (defecto, brecha de verificación, oportunidad, diferencia intencional), la confianza en la evidencia y el estado de avance.

Arrastra al reporte nuevo el registro completo del reporte anterior:
- los asuntos sin resolver que quedaron fuera de la muestra de hoy;
- entradas compactas para los asuntos ya cerrados.

Conserva las marcas de tiempo originales de primera detección y última verificación. Que un asunto no esté entre las tres acciones recomendadas no significa que esté cerrado. Usa estas etiquetas de avance:

| Estado (equivalente en reportes antiguos) | Evidencia requerida |
|---|---|
| Nuevo (New) | Es la primera vez que aparece en este historial. Di "detectado por primera vez", no "introducido recientemente", salvo que la evidencia previa lo demuestre. |
| Sigue abierto (Still open) | Se revisó de nuevo y el defecto o la brecha de verificación continúa, o se confirmó que una oportunidad sigue pendiente. |
| Resuelto (Resolved) | La comprobación de cierre original pasa con evidencia actual. Una edición propuesta, una marca de tiempo cambiada, una copia instalada o un éxito autodeclarado no bastan para declararlo resuelto. |
| Reabierto (Reopened) | Estaba resuelto y se demuestra otra vez la misma falla. Conserva el ID y referencia su cierre anterior. |
| Sin revisar (Not rechecked) | No se cubrió, no fue accesible o la evidencia de hoy es insuficiente. Conserva el último estado verificado; nunca des a entender que se resolvió ni que hay una falla nueva. |
| Ya no aplica (No longer applicable) | Cambiaron explícitamente los requisitos, se retiró el flujo de trabajo o hay otro cambio de alcance con evidencia. Explica por qué; esto no es una reparación exitosa. |

Casos especiales:
- Un hallazgo resuelto antes y no revisado hoy queda como `Sin revisar`, con último estado verificado `Resuelto`. No es un defecto reabierto.
- Si un supuesto defecto anterior se descarta o resulta intencional, registra la corrección y su evidencia en el reporte nuevo. No lo llames reparación ni borres la observación anterior.

Para cada hallazgo registra:
- ID y clase;
- destino y runtime afectados;
- primera detección, estado anterior y estado actual;
- marca de tiempo y estado de la última verificación;
- enlaces a la evidencia;
- comprobación de cierre.

El estado actual siempre corresponde a esta ejecución; no se garantiza que siga igual entre auditorías.

## 3. Explica el avance con honestidad

Usa una tabla de transiciones compacta y una narrativa breve:

| ID del hallazgo | Estado anterior | Esta ejecución | Evidencia / cambio práctico | Próxima comprobación |
|---|---|---|---|---|
| ID estable existente | Estado registrado antes | Uno de los estados de arriba | Evidencia actual, o motivo por el que no se revisó | Comprobación de aceptación original o una revisión justificada |

- **Separa los tipos de cambio:** **arreglos reales**, **evidencia recién verificada**, **regresiones** y **cambios de cobertura o de rúbrica**.
  - Más registros pueden justificar más puntaje sin que el sistema haya mejorado.
  - Un defecto recién descubierto puede bajar el puntaje sin que haya una regresión reciente.
- **Comparación de puntajes:**
  - Si la comparación es válida, muestra los cuatro subtotales anteriores y actuales, los totales brutos, los topes y los totales finales. Explica qué evidencia de qué criterio cambió y el efecto de cualquier tope.
  - Si no lo es, di **los puntajes no son directamente comparables** y explica por qué. No muestres una diferencia ni una tendencia engañosa.
- **Conteos de hallazgos:** muestra los hallazgos únicos por estado de avance, distinguiendo lo que se revisó de nuevo de lo que solo se arrastró.
  - Trata "ya no aplica" y las clasificaciones corregidas por separado de las reparaciones verificadas.
  - No declares una mejora solo porque subió el puntaje o bajó la cantidad de asuntos abiertos.
- **Próximas comprobaciones:** priorízalas según el impacto en el usuario, incluidos los asuntos previos importantes sin resolver. No vuelvas a ejecutar flujos pagados, no envíes alertas ni hagas reparaciones solo para ganar el estado de resuelto.

## 4. Guarda cada ejecución de forma segura

1. **Nombra el archivo.** Usa [la plantilla de reporte](templates/report.md). Genera una marca de tiempo UTC real y un ID de ejecución resistente a colisiones (por ejemplo, la marca de tiempo más un sufijo aleatorio).
   - Nombre de archivo por defecto: `audits/audit-YYYY-MM-DD-HHMMSS-<sufijo>.md`, en UTC.
   - Incluye en los metadatos marcas de tiempo con zona horaria y la raíz auditada exacta.
   - Son registros locales, no publicaciones.
2. **Completa cada sección obligatoria** con evidencia real, o con una explicación explícita de "no revisado" o "parcial".
   - Conserva la aritmética completa de los criterios, el registro de hallazgos actual, los enlaces a reportes previos, los límites de la comparación y las comprobaciones de cierre propuestas.
   - No dejes marcadores de ejemplo ni resultados inventados.
3. **Crea el archivo sin sobrescribir** una ruta existente: usa creación exclusiva o una protección equivalente contra colisiones, y reintenta con un sufijo nuevo si hace falta.
   - Nunca reemplaces en silencio una ejecución anterior del mismo día y conserva las ejecuciones paralelas.
   - No reescribas reportes históricos cuando una ejecución posterior resuelva un asunto: los reportes posteriores documentan la transición.
4. **Relee el reporte guardado.** Verifica:
   - los metadatos y los enlaces a reportes previos;
   - la aritmética del puntaje;
   - los IDs y estados de los hallazgos;
   - que lo sensible esté redactado;
   - que el contenido guardado coincida con el resultado informado.

   Resuelve los enlaces relativos desde la carpeta del reporte. En el chat, enlaza la ruta absoluta del archivo guardado con un resumen breve del avance.
5. **Si la auditoría termina antes de tiempo,** guarda la evidencia observada con `report_status: partial`:
   - los puntajes no disponibles en `null`, con sus razones;
   - los hallazgos no revisados, arrastrados.

   Una ejecución parcial no es una línea base de puntaje completa. Si el proceso termina de forma inesperada, quizá no se pueda guardar; nunca afirmes lo contrario.
6. **Si no se puede escribir en el sistema de archivos,** di **reporte no guardado**, entrega el reporte en el chat y describe el bloqueo específico.
   - No lo reemplaces por un volcado de registros con secretos, no lo guardes en silencio en otro lugar y no digas que se actualizó el historial.
   - Una instrucción explícita del usuario de no guardar tiene prioridad; en ese caso di **no se guardó, a pedido tuyo**.

El espacio de trabajo auditado queda sin cambios, salvo el reporte nuevo y su carpeta.
- No agregues una entrada de auditoría a la memoria del negocio.
- No modifiques `decisions/log.md` en cada auditoría.
- No actualices los manuales automáticamente.

Los reportes existentes son evidencia de un momento dado, nunca hechos actuales y canónicos del negocio.

## Comprobaciones de calibración

- **Primera ejecución:** se guarda un reporte real, sin línea base inventada, sin diferencia de puntaje y sin hallazgos reparados.
- **Segunda ejecución:** el reporte original queda sin cambios, los IDs se arrastran y solo se resuelve con evidencia que pase la comprobación.
- **Ejecuciones en el mismo segundo o en paralelo:** nombres de archivo distintos; ninguna reemplaza a la otra.
- **Alcance reducido:** los hallazgos previos omitidos siguen visibles como sin revisar; no se resuelven automáticamente.
- **Cambio de alcance o de rúbrica:** se pueden mostrar las transiciones de hallazgos, pero no se declara una mejora del puntaje total.
- **Un hallazgo resuelto vuelve a fallar:** se reabre con el ID original y la evidencia actual.
- **Falla de permisos o pedido explícito de no guardar:** no hay confirmación falsa de guardado.
- **Reporte parcial o de fixture:** nunca se usa como línea base de puntaje completa.
