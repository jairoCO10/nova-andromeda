---
audit_kind: aios
history_schema: 1
run_id: "<marca de tiempo UTC y sufijo aleatorio>"
started_at: "<ISO-8601 UTC>"
completed_at: "<ISO-8601 UTC>"
project_root: "<raíz auditada absoluta; usa barras / en las rutas YAML>"
project_identity: "<identidad verificada del proyecto, sin credenciales>"
report_status: complete
rubric_version: v2
previous_reports: []
score_baseline: null
scores_comparable: false
scores:
  context: null
  connections: null
  capabilities: null
  cadence: null
  raw_total: null
  final: null
---

<!-- Las claves y los valores del frontmatter se mantienen en inglés por compatibilidad con el historial de auditorías. report_status: complete | partial. -->

# Auditoría del AIOS: <proyecto y fecha>

## Conclusión y alcance

<Qué funciona, la diferencia más importante, runtimes/flujos/dominios/pruebas inspeccionados, conteos, exclusiones y límites de verificación. Marca explícitamente las ejecuciones parciales.>

## Hallazgos de AGENTS.md / CLAUDE.md

<Manuales exactos revisados / faltantes / no revisados, comparación de la guía compartida, IDs de hallazgos y referencias a archivos, cobertura de manuales con alcance y si se modificaron los manuales.>

## Enrutamiento y compatibilidad de migración

<Matriz de compatibilidad y hallazgos únicos agrupados en defecto confirmado, brecha de verificación, diferencia intencional y oportunidad de mejora. Incluye evidencia de origen y destino, y la cobertura de descubrimiento frente a la de ejecución.>

## Pruebas de enrutamiento

<Cinco preguntas seleccionadas, rutas intentadas, fuentes y resultado: directo / por búsqueda alternativa / sin resolver.>

## Qué funciona

<Hasta tres fortalezas con evidencia.>

## Confiabilidad operativa verificada

<Los 20 IDs de criterio con sus puntos, los cuatro subtotales, el total bruto, los topes con sus razones, el puntaje final y la etapa. Distingue los defectos de la evidencia no verificada. Mide la confiabilidad operativa verificada, no la utilidad general. Las entradas parciales o sin puntaje quedan en null.>

## Avance desde la auditoría anterior

<Enlaces clicables a los reportes previos y línea base de puntaje, o primera línea base registrada. Muestra las transiciones, las reparaciones reales frente a las ganancias solo de evidencia, las regresiones y los cambios de cobertura o de rúbrica. Incluye la aritmética comparable de puntajes solo cuando esté justificada.>

## Registro de hallazgos

| ID | Clase | Destino / runtime | Primera detección | Estado anterior | Estado actual | Última verificación (fecha / estado) | Evidencia | Comprobación de cierre |
|---|---|---|---|---|---|---|---|---|

<Completa con los hallazgos actuales y todos los arrastrados, incluidos los no revisados y los cierres anteriores en forma compacta. No tener hallazgos es válido si el alcance inspeccionado lo respalda.>

## Mejoras principales y próxima ejecución

<Hasta tres acciones priorizadas (reparar / verificar / opcional) con su beneficio, los IDs de hallazgos y las comprobaciones de aceptación. Incluye un prompt acotado para la próxima ejecución y los límites de verificación sin resolver.>
