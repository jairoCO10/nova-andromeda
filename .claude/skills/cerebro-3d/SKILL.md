---
name: cerebro-3d
description: Úsalo cuando alguien pida construir un cerebro 3D, visualizar su AIOS o su Segundo Cerebro, convertir su conocimiento en un grafo interactivo, o ejecute /cerebro-3d. También aplica a pedidos en inglés como "3D brain".
disable-model-invocation: true
argument-hint: "[nombre del cerebro] [categorías o ruta de una app existente]"
---

# Cerebro 3D

Convierte los archivos reales del AIOS del usuario en un globo de conocimiento 3D, local y personalizado. Usa la aplicación que ya viene incluida y funciona; no crees una interpretación nueva de su apariencia. Conserva la composición esférica, las categorías con colores, el orbe central, las partículas sutiles en las conexiones, el modo cine y la repetición interactiva del crecimiento.

El comando es `/cerebro-3d` en Claude Code. En Codex, selecciona el skill `cerebro-3d` o usa `$cerebro-3d`. Interpreta de la misma forma frases naturales como "cerebro 3D" o "3D brain". La entrada viene de `$ARGUMENTS` y de la conversación. Trabaja en el asistente actual: no hacen falta subagentes, servicios externos, claves de API, recursos pagados ni despliegue.

Habla con el usuario en español latinoamericano neutro, salvo que prefiera otro idioma.

## 1. Encuentra el AIOS y el paquete

Lee el manual operativo local correspondiente y el índice relevante. Identifica la raíz real del AIOS; no escanees un directorio superior ajeno ni toda la carpeta personal del usuario. Ubica la carpeta de este skill a partir del `SKILL.md` cargado: todas las rutas del paquete de abajo son relativas a ella, ya sea que esté en `.claude/skills`, `.agents/skills` o en un plugin.

Lee [la especificación portable](references/portable-spec.md) y [la guía de configuración](references/config.md). Verifica que haya Node.js 22 o superior, usando el runtime que el usuario ya tiene. Si no está disponible, explica que Node es necesario y sigue la política de instalación y aprobación del entorno.

Ejecuta el asistente de descubrimiento, que solo lista rutas:

```text
node <carpeta-del-skill>/scripts/discover.mjs --root <raíz-del-AIOS>
```

Lista carpetas candidatas sin leer su contenido. Usa también las rutas explícitas del manual operativo para encontrar carpetas personalizadas de wiki, reuniones, videos o proyectos. No supongas que los nombres de carpeta o las cuentas del autor existen en este equipo.

## 2. Pregunta el nombre y las categorías

Usa la herramienta de preguntas del entorno si existe; si no, pregunta en lenguaje natural. Reutiliza la información que ya te dieron y no repitas preguntas respondidas.

1. **Nombre:** "¿Cómo quieres llamar a tu cerebro 3D?" Acepta el nombre exacto que se mostrará, por ejemplo "Cerebro de Atlas", "Mente Estudio" o "El Segundo Cerebro de Maya". No elijas en silencio el nombre ni la marca del autor. Un argumento del comando puede responder esta pregunta.
2. **Categorías:** "¿Qué categorías principales quieres ver?" Ofrece las categorías que realmente encontraste, cada una con la ruta de archivo o carpeta propuesta. Por ejemplo: Conocimiento del negocio, Reuniones, Conocimiento de videos, Memoria de Claude, Memoria de Codex, Proyectos y Skills. Deja que el usuario renombre, quite o agregue categorías. Sugiere entre tres y siete para que se vea claro; se admiten de una a doce.

La respuesta sobre las categorías también aprueba las rutas listadas. Si hay una categoría personalizada con una ruta desconocida, pregunta dónde están esos archivos. No adivines raíces de memoria externas.
- La memoria curada de Codex puede abarcar varios proyectos: aclara ese alcance al ofrecerla e inclúyela solo si la eligen.
- La memoria de Claude debe apuntar a la carpeta de memoria de este AIOS, no a todos los proyectos de Claude.

Muestra en tu actualización de avance el mapa compacto de nombre, categorías y rutas. Con esas respuestas, sigue construyendo sin pedir otra confirmación genérica. Pregunta solo por rutas sin resolver, por reemplazar una app existente o por otra ambigüedad importante.

## 3. Genera exactamente la experiencia incluida

Salida por defecto: `<raíz-del-AIOS>/apps/3d-brain/`. Este nombre de carpeta se mantiene en inglés por compatibilidad con instalaciones existentes.
- Si la carpeta ya existe, revisa su `brain.config.json` y reutiliza la app. No la sobrescribas a ciegas.
- Si piden reemplazarla, primero archiva la versión existente dentro del mismo proyecto.
- Si la ocupan archivos que no tienen relación, elige otra carpeta o pregunta al usuario.

Crea un archivo JSON de configuración en una carpeta temporal ignorada dentro del AIOS del usuario, con el esquema de [config.md](references/config.md):
- No incluyas el contenido de ninguna nota.
- Usa rutas relativas para las fuentes dentro del AIOS y rutas explícitas y aprobadas para las fuentes externas.
- Asigna a cada categoría un ID único, una etiqueta, un color, un adaptador y una o más rutas reales.

```text
node <carpeta-del-skill>/scripts/scaffold.mjs --root <raíz-del-AIOS> --config <json-de-configuración> --out apps/3d-brain
```

Esto copia una lista explícita de archivos de la aplicación, escribe la configuración personalizada local y se niega a usar una carpeta de destino existente.

El renderer viene precompilado: `node serve.mjs` funciona sin instalar nada con npm. No copies a la app ni al skill `node_modules`, la configuración de otro usuario, una instantánea del grafo, capturas, archivos de memoria ni registros de sesión.

En la carpeta de la app generada:

```text
node build.mjs
node serve.mjs
```

Inicia el servidor con el mecanismo normal del entorno para procesos en segundo plano. En Windows, esos procesos deben iniciarse ocultos. El puerto por defecto es 4640:
- Si está ocupado, elige uno libre, actualiza la configuración de esta app e inicia ahí.
- Nunca detengas un servicio ajeno.
- Mantén la dirección de escucha en `127.0.0.1`.

Lee los conteos y avisos reales de la construcción:
- Una carpeta faltante es un problema de configuración que hay que resolver, no una razón para inventar nodos.
- Las categorías vacías están permitidas y se muestran tal cual.
- Si todo el AIOS está vacío, explica que necesita notas guardadas. No lo llenes con contenido sintético, salvo que el usuario pida por separado un ejemplo claramente etiquetado.

## 4. Conserva el comportamiento y las conexiones reales

El renderer incluido es el contrato visual. Conserva:

- Un globo estable, colores distintos por fuente, fondo oscuro, orbe central brillante y acentos orbitales sutiles.
- Enlaces reales: enlaces Markdown explícitos y wikilinks. Las menciones por título exacto se distinguen de las relaciones explícitas, y los enlaces ambiguos quedan sin resolver.
- Búsqueda, activar o ver solo una fuente, inventario, indicadores de salud, lectura de notas y mostrar el archivo local.
- **Reproducir demo:**
  - Empieza con una idea central y sigue con la primera conexión real.
  - Las ramas brotan de sus nodos padre y el crecimiento se acelera hasta mostrar el cerebro completo en unos 29 segundos.
  - Las notas desconectadas se suman sin aristas inventadas.
  - Es una repetición de la conectividad, no una cronología histórica.
- El orbe central es visible desde el primer fotograma. Arrastrar, hacer zoom o hacer clic en el lienzo no detiene el crecimiento. Si el usuario mueve la cámara, eso reemplaza el alejamiento automático. Al repetir, todo se reinicia limpio.
- **Modo cine:** presentación limpia, con el contador de crecimiento junto a la escena. Deben funcionar la pausa de movimiento, el soporte de movimiento reducido y los controles de fuente adaptables, y no deben quedar etiquetas viejas después de repetir.

Toda la interfaz con el nombre sale de `brain.config.json`. La interfaz está en español y lleva la marca discreta "Andromeda AI · adaptado por Miguel Silva" en la pantalla de inicio y en el título de la pestaña. Consérvala. No regeneres los visuales con un modelo de imágenes ni reemplaces la escena por un grafo de fuerzas genérico. Si hace falta cambiar código, usa `npm ci`, edita `src/` y ejecuta `npm run build:js`. Mantén los avisos de licencia de las dependencias junto al bundle.

Los adaptadores por defecto leen Markdown, texto y la memoria curada de Codex. Para Google Drive, Notion, JSON de reuniones sin procesar, bases de datos, PDFs u otra fuente no compatible, explica la limitación y usa una exportación local aprobada explícitamente, o construye y prueba un adaptador. No digas que esos sistemas están conectados solo porque sus nombres aparecen en una categoría.

## 5. Verifica y entrega

Sigue [la lista de aceptación](references/acceptance.md). Revisa la app generada real, no solo la plantilla:

1. La API del grafo tiene el nombre y las categorías pedidas, IDs únicos, extremos válidos y conteos que coinciden con el escaneo de fuentes.
2. Lee al menos una nota real de cada categoría no vacía, incluidas las secciones temáticas exactas de la memoria de Codex. Los originales quedan sin cambios.
3. Confirma el nombre personal en la página y prueba la búsqueda, el filtro de una sola fuente, la restauración y el inventario.
4. Observa el crecimiento al inicio, a la mitad y al final. Arrastra y haz zoom mientras el contador sube. Revisa el orbe inicial, que las etiquetas estén limpias, el conteo final completo y que repetir reinicie bien. Prueba el modo cine y la pausa y reanudación.
5. Revisa la vista de escritorio y una vista angosta. No manipules el mouse físico del usuario: el bloqueo nativo del puntero está desactivado en la app incluida. La automatización del navegador debe ser virtual o sin interfaz.
6. Revisa los errores de consola. Si no puedes verificar en el navegador, di exactamente qué comprobaciones quedaron sin verificar, en lugar de afirmar que todo se ve bien.

Agrega una ruta breve al README de la app nueva en el índice de proyectos o en el manual operativo del AIOS, siguiendo sus convenciones. Sincroniza `AGENTS.md` y `CLAUDE.md` cuando corresponda. No guardes configuraciones privadas, datos del grafo ni contenido de notas en un repositorio público. No despliegues ni hagas push sin autorización del usuario.

Termina con:
- el nombre del cerebro, el enlace local y la carpeta de la app;
- los conteos reales de notas y categorías;
- las instrucciones más breves que sirvan: **Reproducir demo**, **Modo cine**, arrastrar para girar, desplazarse para hacer zoom.

Menciona si faltaron fuentes. Nunca prometas viralidad.
