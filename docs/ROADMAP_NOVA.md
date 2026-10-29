# Rumbo de NOVA

## Principios

- El perfil, los recuerdos y los planes identifican su fuente, fecha y alcance: usuario, equipo o servicio.
- Las acciones locales comienzan en modo de solo lectura. NOVA explica qué va a hacer antes de escribir, borrar o enviar.
- Cada integración tiene permisos y estado propios. Un dato de perfil no se convierte por sí solo en autorización para actuar.
- El Cerebro 3D y el móvil consumen las mismas interfaces de NOVA; no mantienen memorias divergentes.

## Etapas

1. **Perfil y mantenimiento:** formulario local, copia previa, corrección de datos y separación entre perfil general, datos privados y recuerdos de SQLite.
2. **Herramientas del equipo:** hora local, espacio en disco y procesos/recursos con informes de solo lectura; las acciones de cierre o borrado requieren confirmación.
3. **Información actualizada:** proveedores explícitos para clima y mercados, con hora de consulta y fuente visibles.
4. **Correo y calendario:** conexión por OAuth con permisos mínimos. Primero lectura y búsqueda; crear eventos, recordatorios o enviar mensajes requiere confirmación.
5. **API y móvil:** una API autenticada con transmisión de respuestas en tiempo real, emparejamiento de dispositivos y conexiones cifradas. Acceso remoto solo por una red privada o un túnel protegido.
6. **Cerebro 3D móvil:** cliente adaptable que consulta el mismo grafo local autorizado y refleja las fuentes que NOVA puede leer.

## Transporte

Ollama conserva su API HTTP local: es la interfaz que ofrece el servicio del modelo, no una consola. Para transmitir respuestas parciales al navegador o a Android, NOVA puede exponer WebSocket sobre una conexión autenticada y cifrada. No se abre un puerto público sin emparejamiento, autenticación y una capa de transporte segura.
