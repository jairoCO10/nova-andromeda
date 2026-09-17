# Tu Cerebro 3D

Una vista local y de solo lectura de las fuentes de conocimiento seleccionadas en `brain.config.json`. Forma parte de Andromeda AI, una adaptación de AIS-OS en español.

Ejecuta `node serve.mjs` desde esta carpeta y abre el enlace localhost que aparece en la consola. Requiere Node.js 22 o superior. El renderer ya viene compilado, así que no hace falta instalar nada para usarlo. Para modificarlo, ejecuta `npm ci`, edita `src/` y luego `npm run build:js`.

El nombre, las categorías, los colores, las rutas de origen y el puerto se definen en `brain.config.json`. **Reconstruir desde el disco** (en el inventario) actualiza las notas y las conexiones. Si cambias el código o el puerto, reinicia el servidor. Si una fuente falta o no se puede leer, aparece como aviso en el inventario; nunca se inventan notas.

- Arrastra para girar, desplázate para hacer zoom y haz clic en un nodo para leerlo. La tecla `/` activa la búsqueda.
- Los botones de fuente activan o desactivan categorías. Con Shift + clic ves solo una; si haces clic en la última fuente activa, vuelven a mostrarse todas.
- **Reproducir demo** (`D`) hace crecer el grafo siguiendo conexiones reales durante unos 29 segundos. Mientras crece puedes seguir girando y haciendo zoom. El orbe central es visible desde el inicio. Al terminar, puedes repetirla.
- **Modo cine** (`C`) oculta la interfaz alrededor. Escape lo cierra.
- El botón de movimiento pausa la rotación y los acentos animados. Se respeta la preferencia de movimiento reducido del sistema.
- Solo los vecindarios seleccionados muestran caminos resaltados; en la vista general, las conexiones se muestran por muestreo para que se lean bien. El inventario conserva los totales completos.

La repetición muestra cómo se conectan las notas, no cuándo se crearon. Las relaciones desconocidas quedan sin conectar. Las coincidencias exactas de título se etiquetan como "mención"; los enlaces Markdown explícitos y los wikilinks tienen prioridad. Si hay archivos con el mismo nombre y un enlace ambiguo, se informa en lugar de asignarlo en silencio.

Lee directamente archivos Markdown y de texto, incluidas notas locales de reuniones, páginas de wiki, notas de proyectos, skills y la memoria de Claude. El adaptador de Codex lee resúmenes de memoria curados, grupos temáticos, recapitulaciones y notas de flujos de trabajo; excluye los registros de sesión sin procesar y las exportaciones duplicadas de memoria. Los sistemas remotos, PDFs, bases de datos y el JSON sin procesar de reuniones necesitan una exportación local explícita o un adaptador adicional: esta app no los procesa automáticamente.

El servidor escucha en `127.0.0.1`:
- Solo expone los IDs de las notas indexadas y los recursos estáticos aprobados.
- Rechaza solicitudes de API de otros orígenes y sanea el Markdown que muestra.
- El bloqueo nativo del puntero y la captura del cursor están desactivados.
- Nunca modifica los archivos de origen.
- La configuración local y el grafo generado están en `.gitignore`.

El modo cine oculta los controles, no la información privada: revisa las notas visibles antes de grabar o compartir capturas.

Las licencias de las dependencias de terceros están en `THIRD-PARTY-NOTICES.txt`.
