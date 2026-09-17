# Enrutamiento y compatibilidad entre runtimes

Obligatorio en cada auditoría. Mantén las comprobaciones acotadas y de solo lectura.
- Inspecciona los runtimes que realmente se usan o que se quieren migrar explícitamente. Un proyecto con un solo runtime no necesita instalaciones duplicadas para aprobar.
- Trata una posible migración futura como una oportunidad opcional, salvo que la pidan.
- Nunca instales, sincronices, renombres ni ejecutes flujos de trabajo del proyecto solo para auditarlos.

## 1. Define el contrato de comparación

- **Lee la configuración del proyecto:** los manuales aplicables, las anulaciones con alcance, la documentación de puentes y la configuración de sincronización. Identifica:
  - la fuente canónica;
  - las copias generadas;
  - las implementaciones independientes intencionales;
  - las reglas de uso compartido declaradas.

  No supongas que el archivo más nuevo o la copia de Claude es la autorizada.
- **Inventaria las ubicaciones reales de skills del proyecto,** incluidas `.claude/skills`, `.agents/skills` y `.codex/skills` cuando existan o se mencionen. Una carpeta literal `.agent/skills` es una posible errata o ubicación personalizada, no automáticamente una raíz de skills descubierta: verifícala contra el runtime instalado.
  - En esta distribución, `.claude/skills` es la fuente canónica y `.agents/skills` se genera con `scripts/sync-codex-skills.sh`, que solo cambia las rutas `.claude/skills/` → `.agents/skills/` en archivos `.md`.
- **Incluye las raíces a nivel de usuario relevantes,** los directorios enlazados, las anulaciones de runtime y los nombres duplicados, cuando estén disponibles mediante descubrimiento o configuración.
  - No recorras archivos personales sin relación ni expongas secretos de configuración.
  - Si el descubrimiento a nivel de usuario no está disponible, informa esa limitación.
- **Establece el descubrimiento y la precedencia** con el listado o la configuración de solo lectura del runtime instalado o, si hace falta, con la documentación oficial vigente.
  - Que exista una carpeta no prueba ni disponibilidad ni precedencia.
  - Registra el runtime y su versión cuando estén disponibles.
  - No supongas que cada ubicación listada funciona en todas las versiones.
  - En Claude Code, el comando de un skill de proyecto sale del nombre de su carpeta y no hay aliases.
- **Informa el alcance con números:**
  - manuales leídos;
  - raíces inventariadas;
  - skills comparados y skills con descubrimiento verificado;
  - recursos revisados y flujos de trabajo ejecutados.

  Indica qué se muestreó o se omitió. Una revisión de metadatos no es una prueba de ejecución.

## 2. Compara las instrucciones operativas

1. **Qué comparar:** los `AGENTS.md` y `CLAUDE.md` de la raíz cuando existan, y después las anulaciones con alcance muestreadas. Compara:
   - propósito y preferencias del usuario;
   - autoridad de las fuentes y rutas;
   - ubicaciones de salida y permisos;
   - instrucciones de flujos de trabajo.
2. **Clasifica cada diferencia importante** como:
   - guía compartida que coincide;
   - adaptación intencional del runtime;
   - conflicto u omisión confirmados;
   - diferencia sin resolver.

   Los espacios en blanco y los finales de línea no son conflictos de comportamiento. Exige sincronización exacta solo cuando el proyecto la prometa explícitamente, e informa la deriva de formato inofensiva como tal.
3. **Manual faltante:** es un defecto de migración solo si, por eso, el runtime de destino queda sin la guía necesaria y ningún puente o equivalente verificado la aporta. No exijas manuales duplicados en una configuración de un solo runtime.
4. **Cómo reportar:** muestra las referencias de archivo y línea de ambos lados, las reglas que difieren, el runtime afectado y el comportamiento probable. En las omisiones, cita la regla de origen y la sección o archivo de destino inspeccionado. Nunca inventes una línea de destino para un texto ausente.
5. **Puentes:** revisa que conserven las instrucciones compartidas sin aparentar que se aplican campos o herramientas que el runtime no admite. Los nombres distintos de modelos o herramientas pueden ser adaptaciones válidas; perder un límite de aprobación o una ruta de fuente sí es sustancial.

## 3. Revisa las rutas en ambos sentidos

- **De la ruta al destino:** resuelve las rutas concretas desde la base correcta (repositorio, archivo que la contiene, directorio de trabajo declarado, carpeta del usuario o un host separado) y verifica que existan y lleven al destino previsto.
  - Distingue las referencias concretas de los marcadores, ejemplos, globs, URLs y rutas de hosts remotos.
  - Una ruta remota que no está disponible localmente queda sin verificar; no es automáticamente una ruta rota.
- **Del destino importante a la ruta:** compara los índices y manuales relevantes con los inventarios inmediatos de proyectos, conocimiento y skills.
  - Sigue las cadenas de índices: un proyecto anidado puede estar bien enrutado sin un enlace directo desde el manual raíz.
  - Identifica material activo y útil que no tenga una ruta de entrada utilizable, con evidencia de su relevancia.
  - Una carpeta sin clasificar es una candidata a revisar, no automáticamente un huérfano.
- **Problemas frecuentes a revisar:**
  - nombres de usuario obsoletos y carpetas movidas;
  - rutas absolutas específicas de una plataforma;
  - errores de ortografía o de mayúsculas relevantes en carpetas;
  - alias o conteos desactualizados;
  - material archivado presentado como activo;
  - enlaces que apuntan a un destino válido pero equivocado. Una ruta que existe puede estar mal igual.
- **Exclusiones:** no marques cada archivo sin enlace. Los archivos temporales, generados, las dependencias, los archivados y el material intencionalmente privado o especializado pueden estar bien excluidos. Distingue el contenido desactualizado de un archivo viejo cuyo contenido sigue siendo correcto.

## 4. Compara los paquetes de skills y su disponibilidad real

Empareja los skills por su identidad declarada, su propósito y sus aliases documentados, no solo por el nombre de la carpeta. Si el proyecto renombró skills (como esta distribución, que pasó de `onboard`/`audit`/`grill-me`/`link`/`level-up`/`3d-brain` a `empezar`/`auditar`/`entrevistame`/`conectar`/`subir-nivel`/`cerebro-3d`), trata el cambio documentado como intencional. Haz un inventario amplio por metadatos y después inspecciona los recursos necesarios para los flujos de trabajo seleccionados y cualquier diferencia sospechosa.

1. **Presencia:** la copia de origen o de destino requerida, o un alcance intencionalmente específico de un runtime.
2. **Contenido:** los pasos compartidos del flujo de trabajo, las entradas, las salidas, los límites y el comportamiento.
   - En los espejos declarados, compara después de aplicar solo las transformaciones documentadas.
   - Nunca elimines en bloque el texto específico del runtime ni las diferencias de rutas para fabricar una coincidencia.
3. **Recursos:** los scripts, plantillas, ejemplos, assets, instrucciones de dependencias y referencias de agentes necesarios deben resolverse desde el entorno de destino.
   - Incluye los archivos obsoletos que sobren en el espejo como posible deriva: una comparación solo de origen a destino no los detecta.
   - Los enlaces simbólicos rotos y los destinos fuera de la copia necesitan evidencia explícita.
4. **Descubrimiento:** distingue entre presente en disco, listado por el runtime, desactivado y no revisado.
   - Detecta identidades duplicadas entre las raíces del proyecto y del usuario, y determina cuál se usa en la práctica cuando se pueda.
   - Si no se puede verificar la precedencia, informa la ambigüedad.
   - No supongas que aparecer en un menú significa que se ejecuta con éxito.
5. **Comportamiento:** revisa llamadas a herramientas incompatibles, instrucciones no admitidas, directorios de trabajo incorrectos, comandos de plataforma, nombres de variables de entorno faltantes (sin revelar sus valores) y dependencias no documentadas.
   - Para la ejecución real, usa evidencia existente y segura.
   - Deja sin probar los flujos pagados, las publicaciones y otros flujos con efectos secundarios en una auditoría de solo lectura.

## 5. Comunica el resultado

Usa estas clases de hallazgo:

- **Defecto confirmado:** la evidencia muestra una ruta o un recurso requerido que falta, una instrucción en conflicto, una ruta rota o un skill requerido que no está disponible.
- **Brecha de verificación:** no se estableció el descubrimiento, el acceso remoto, la intención o la ejecución. Indica la comprobación más pequeña que lo resolvería.
- **Diferencia intencional:** una adaptación del runtime documentada y apropiada. No necesita reparación.
- **Oportunidad de mejora:** una simplificación o extensión útil sin una falla demostrada. Explica el beneficio sin decir que algo está roto.

Muestra una matriz de compatibilidad compacta, con las rutas y los nombres de runtime reales:

| Elemento | Evidencia en Claude | Evidencia en Codex | Hallazgo / ID | Consecuencia práctica |
|---|---|---|---|---|
| Guía operativa compartida | Archivo / sección | Archivo / sección o puente verificado | Coincide / diferencia intencional / conflicto / no revisado | Qué cambia para el usuario |
| Skill muestreado | Estado del paquete canónico | Estado del espejo / descubrimiento | Equivalente / falta / deriva / desactivado / no revisado | Qué funciona o falla al cambiar de runtime |
| Recurso o ruta requerida | Origen resuelto | Destino resuelto | Válido / roto / sin enlace / no revisado | Efecto en la recuperación o la ejecución |

Después muestra solo los hallazgos accionables, agrupados por clase:

| ID / clase / prioridad | Evidencia y runtime afectado | Impacto en el usuario | Cambio o verificación propuesta | Comprobación de cierre |
|---|---|---|---|---|
| ID estable; reparar, verificar u oportunidad | Pares exactos de archivo y línea, o resultado fechado del runtime | Falla concreta o incertidumbre | Edición canónica / sincronización / ruta nueva / comprobación de solo lectura | Resultado observable |

**Prioriza y agrupa:**
- Las respuestas incorrectas, las instrucciones perdidas, los flujos de trabajo no disponibles y la deriva insegura de permisos van antes que las diferencias cosméticas.
- Usa un solo ID para un mismo problema de fondo en las secciones de manual, enrutamiento y skills.
- No ocultes un defecto confirmado de menor prioridad solo porque se recomiendan tres acciones.

**Conclusión de la migración muestreada:**
- **Bloqueada:** solo ante un defecto confirmado que impida un comportamiento migrado requerido.
- **Necesita verificación:** si hay evidencia sin resolver o una diferencia confirmada que no bloquea.
- **Aprobó las comprobaciones inspeccionadas:** cuando las comprobaciones indicadas pasaron sin hallazgos aplicables sin resolver. Las oportunidades opcionales no impiden aprobar.

Siempre nombra la ejecución y la cobertura que no se revisaron.
- No agregues un quinto puntaje ni un porcentaje de migración.
- No des bonificación por archivos duplicados.
- No hagas reparaciones automáticas.

## Casos de calibración

- **Mismas reglas, distintos nombres de herramientas admitidas:** los manuales comparten todas las reglas pero usan nombres distintos de herramientas admitidas. Es una adaptación intencional, no un conflicto.
- **Solo difiere el final de línea:** el proyecto promete explícitamente manuales idénticos y solo difiere la codificación de los saltos de línea. Es solo formato, no un bloqueo de comportamiento.
- **Regla de permisos sin puente:** una regla de permisos compartida existe solo en el manual de origen, sin puente en el destino. Es una omisión confirmada: cita el origen y el destino inspeccionado.
- **Un solo runtime:** el proyecto tiene un solo manual y un solo árbol de skills. No hay penalización por copias faltantes.
- **Skill instalado a nivel de usuario:** el runtime de destino solicitado lista un skill con el mismo nombre desde una instalación de usuario verificada. No falta solo porque no esté su espejo en el proyecto: inspecciona el paquete que se usa en la práctica.
- **Espejo sin una plantilla requerida:** el espejo coincide con la reescritura de rutas documentada, pero le falta una plantilla requerida. Es un defecto confirmado del paquete, aunque el SKILL.md coincida.
- **Precedencia desconocida:** hay skills duplicados en el proyecto y en el usuario, pero no se sabe cuál tiene precedencia. Es ambigüedad o brecha de verificación, no una sobrescritura supuesta.
- **Host remoto no disponible:** un host remoto referenciado no estaba disponible durante la inspección. Es una brecha de verificación, no una ruta local rota.
- **Enrutamiento indirecto:** un proyecto relevante se alcanza mediante un índice de dominio, así que está enrutado. Un archivo temporal sin enlaces entrantes no es un defecto.
- **Listado pero no ejecutado:** un skill está listado y activado, pero no se ejecutó. El descubrimiento está verificado; la ejecución, no.
