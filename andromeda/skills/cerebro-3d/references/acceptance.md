# Lista de aceptación

Verificación del paquete: ejecuta `node <carpeta-del-skill>/scripts/test-package.mjs`. Crea un AIOS ficticio aparte, genera la app, revisa los datos personalizados y los enlaces entre fuentes, verifica que el servidor sea de solo lectura y respete los límites de rutas, y prueba los módulos reales de crecimiento. Nunca usa notas privadas del autor.

En una ejecución real del skill, guarda un pequeño reporte de verificación junto a la app generada. No incluyas su grafo privado ni sus capturas en el skill público.

- [ ] El nombre elegido aparece exacto en el título del documento, el encabezado, la pantalla de inicio y la leyenda de la demo.
- [ ] Las categorías corresponden a las carpetas aprobadas, y los avisos indican qué datos faltan o no son compatibles.
- [ ] Todos los IDs de nodo son únicos, todas las aristas tienen extremos existentes y los archivos con el mismo nombre siguen siendo nodos distintos.
- [ ] La lectura de notas de muestra coincide con los originales, incluidos los límites de temas de Codex.
- [ ] Funcionan la búsqueda, el filtro de una sola fuente, la restauración y el inventario.
- [ ] Al iniciar el crecimiento aparecen un solo nodo y el orbe central, y luego la primera arista real.
- [ ] A mitad del crecimiento se ven ramificaciones y los contadores suben; no queda ninguna etiqueta vieja atrapada en el centro.
- [ ] Arrastrar, hacer zoom y hacer clic en el fondo o en un nodo no detienen el crecimiento.
- [ ] Al terminar se alcanza el número real de nodos visibles, todas las posiciones finales coinciden con el globo y "Repetir demo" arranca limpio.
- [ ] Funcionan el modo cine, la pausa y reanudación, el comportamiento con movimiento reducido y la vista angosta.
- [ ] Se revisan los errores de consola, el servidor escucha solo en loopback y no expone rutas arbitrarias del sistema de archivos.
- [ ] El paquete público contiene solo archivos de runtime y plantilla, y fixtures ficticios; nada de datos personales.

Si alguna capacidad no se puede verificar en el equipo disponible, informa esa limitación exacta. No reemplaces una revisión en el navegador por la confianza de quien implementó.
