# Especificación portable del Cerebro 3D

Este paquete conserva una aplicación que ya funciona, en lugar de depender de una recreación descrita solo en texto. El runtime portable tiene una capa de ingesta configurable y el mismo renderer esférico, planificador de crecimiento, escena orbital y comportamiento de interacción que la implementación de referencia.

## Archivos y contratos

- `assets/template/config.mjs`: valida nombres, IDs de categoría, rutas, colores y límites.
- `assets/template/build.mjs`: lee solo las fuentes locales seleccionadas. Crea los nodos del grafo, aristas basadas en evidencia, indicadores de salud, el inventario y un registro interno de archivos.
- `assets/template/serve.mjs`: servidor Node sin dependencias. Escucha solo en loopback y sirve únicamente los recursos estáticos permitidos. Los IDs de nota se resuelven mediante el registro de archivos, nunca desde una ruta arbitraria de la URL.
- `assets/template/codex-memory.mjs`: importador de solo lectura para la memoria curada, con límites exactos por sección temática.
- `assets/template/src/app.js`: búsqueda, interacción con el grafo, controles de fuentes, paneles, renderizado seguro de notas, modo cine y reproducción del crecimiento. Aquí están los textos de runtime de la interfaz, en español.
- `assets/template/src/constellation.js`: ubicación esférica determinista, orbe central y acentos orbitales sutiles.
- `assets/template/src/growth.js`: un bosque de expansión que usa solo aristas existentes, con ramificación limitada por paso, movimiento con resorte y posiciones finales exactas.
- `assets/template/dist/app.js`: renderer precompilado. No hace falta instalar paquetes para ejecutar la app generada. **Después de editar `src/`, recompila con `npm run build:js`**; de lo contrario, la app seguirá mostrando los textos anteriores.
- `scripts/discover.mjs`: lista rutas candidatas sin leer su contenido.
- `scripts/scaffold.mjs`: copia una lista explícita de archivos permitidos a una carpeta nueva para la app, no sobrescribe carpetas existentes y escribe la configuración local.

## Contrato visual y de interacción

Espacio casi negro, un color por categoría, una silueta esférica desde cualquier ángulo, un orbe central de alambre y dos órbitas sutiles. Las partículas blancas resaltan los caminos seleccionados; las conexiones de fondo se muestran por muestreo. Las etiquetas detectan colisiones y se limpian de forma explícita cuando los nodos se eliminan o se reconstruyen.

El crecimiento empieza con un nodo en el orbe y la primera arista real. Los nodos nuevos brotan de sus nodos padre reales, y una cola de ramificación limitada hace que el grafo crezca hacia afuera en vez de estallar desde un solo nodo central. El crecimiento se acelera, termina en unos 29 segundos, devuelve cada nodo a su posición determinista en el globo y ofrece repetir la demo. Los componentes desconectados tienen raíces independientes.

La órbita y el zoom de la cámara siguen funcionando durante el crecimiento. La interacción del usuario reemplaza el alejamiento automático sin detener la línea de tiempo. El orbe está visible desde el primer fotograma; los anillos aparecen y se expanden después. El modo cine muestra el contador junto al globo. Con la preferencia de movimiento reducido se muestra directamente el estado final estático, sin forzar movimiento.

La vista general dibuja caminos por muestreo. Al seleccionar un nodo se muestran hasta 72 caminos y 24 con partículas; los totales completos siguen disponibles en el inventario. Por defecto, las etiquetas se limitan a un nodo central por categoría y a un vecindario seleccionado pequeño. En móvil, los filtros siguen disponibles con el botón Fuentes.

## Integridad de datos y límites

Los IDs incluyen la categoría y la identidad del archivo, así que dos archivos con el mismo nombre no chocan. Los wikilinks se resuelven solo cuando no son ambiguos. Los enlaces explícitos a archivos tienen prioridad sobre las menciones inferidas. Las menciones por título completo se etiquetan aparte y no implican certeza semántica. La repetición representa conectividad, nunca fechas de creación inventadas.

No se incluye contenido de usuarios, instantáneas de grafos, credenciales, claves de API, exportaciones reales de memoria ni rutas absolutas del equipo del autor. Las configuraciones de usuario y los datos generados quedan en el equipo local y git los ignora. El skill no promete despliegue, compatibilidad universal de formatos, historial exacto ni viralidad.
