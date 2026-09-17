# Verificación del paquete

## Verificación de la adaptación Andromeda AI

Verificado el 17 de septiembre de 2026 en Windows 11 con Node.js 22.16.0, después de localizar la interfaz al español y recompilar `dist/app.js`.

- `node scripts/test-package.mjs` pasó (8 notas) en `.claude` y `.agents`. Con `--demo` también pasó (188 notas, 5 categorías, 545 conexiones).
- Se revisó en el navegador una app ficticia "Atlas Brain" en escritorio y en una vista angosta (406 px):
  - pantalla de inicio con la línea "Andromeda AI · adaptado por Miguel Silva";
  - inventario, panel de nota y lectura de nota, búsqueda sin resultados, filtro de una sola fuente y restauración;
  - pausa de movimiento;
  - demo completa hasta 188/188 con "Repetir demo", y modo cine.
- No hubo errores en la consola.
- Si el panel del navegador está oculto, `requestAnimationFrame` se pausa y la demo parece detenida. Esto no es un error de la app.

## Verificación original (upstream, en inglés)

Verificado el 6 de septiembre de 2026 por el autor original, en Windows con Node.js 24.15.0.

### Comprobaciones automáticas

El paquete de Claude instalado pasó el fixture ficticio grande: **188 notas, cinco categorías configuradas y 545 conexiones**. La copia de Codex pasó el fixture pequeño de ocho notas. Se dejó una categoría ausente a propósito para verificar que aparezca un aviso honesto y un conteo en cero.

Se cubrieron:
- validación de la configuración, creación de la carpeta nueva y rechazo a sobrescribir;
- branding y categorías personalizadas, IDs únicos y archivos con el mismo nombre;
- extremos de aristas válidos, destinos de enlaces relativos y secciones exactas de Codex;
- exclusión de archivos privados;
- orden de padres del crecimiento y posiciones finales;
- lectura HTTP de cada nota, límites de rutas estáticas y de API, y rechazo por Host/Origin;
- archivos fuente sin cambios.

Iniciar el runtime no requirió instalar paquetes de npm.

### Comprobaciones en el navegador

Se revisó una app ficticia aparte, Atlas Brain, en escritorio y a 390 píxeles de ancho. Funcionaron:
- la búsqueda y la lectura de notas;
- un enlace Markdown relativo que abría Launch Plan;
- el filtro de una sola categoría y su restauración;
- los avisos del inventario y el control Fuentes en móvil.

El nombre aparecía en el título, el encabezado, la pantalla de inicio y la leyenda de crecimiento.

El crecimiento en modo cine se observó al inicio, a la mitad y con las 188 notas:
- el orbe central era visible desde el principio;
- arrastrar y hacer zoom de forma virtual no interrumpía la reproducción;
- al terminar se ofrecía repetir;
- al reiniciar se limpiaban las etiquetas anteriores.

El navegador no mostró errores de consola durante los flujos revisados.

El bundle final también pasó una prueba de regresión en el navegador para la navegación por enlaces relativos y la restauración de filtros. El último ajuste del lector de enlaces no modificó los módulos de diseño, animación ni ubicación del grafo.

### Límites

Esto verifica el paquete y los fixtures ficticios en este equipo. No se probaron de forma independiente:
- una ejecución conversacional del skill;
- otros sistemas operativos y Node 22;
- la emulación de movimiento reducido del sistema operativo;
- grafos en el máximo configurado.

Las rutas reales y las categorías de cada usuario siguen necesitando la lista de aceptación. Las capturas y los fixtures quedan como artefactos locales de prueba, fuera de este paquete público.
