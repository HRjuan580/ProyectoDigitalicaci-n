1. Ciclo de Vida del Dato (5b)
¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
En el proyecto, los datos siguen un ciclo de vida bien definido:

-Generación: Los datos son generados por sensores IoT (medidores de energía) y enviados al servidor mediante el protocolo MQTT.

- Almacenamiento: Los datos se almacenan en una base de datos SQLite (o PostgreSQL en producción) con un registro de la marca de tiempo y el valor de consumo.

- Procesamiento: Los datos se utilizan para generar gráficos en tiempo real, alertas y recomendaciones de ahorro energético.

- Archivado: Las tareas completadas o los datos antiguos se archivan después de un período determinado (por ejemplo, 30 días).

- Eliminación: Los datos archivados pueden eliminarse automáticamente después de un tiempo para liberar espacio (esto se puede implementar con un script de limpieza programado).

¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

- Validación de Datos: Los datos recibidos desde los sensores se validan para asegurar que sean numéricos y estén dentro de un rango razonable.

- Transacciones en la Base de Datos: Se utilizan transacciones para garantizar que las operaciones de inserción o actualización se completen correctamente.

- Backups Periódicos: Se realizan copias de seguridad de la base de datos para prevenir pérdidas de datos.

Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

Si el proyecto no trabajara con datos, se podría integrar un sistema de recopilación y análisis de datos. Por ejemplo:

- Agregar sensores IoT para recopilar datos en tiempo real.

- Usar una base de datos en la nube (como Firebase o AWS DynamoDB) para almacenar y gestionar datos de manera eficiente.

2. Almacenamiento en la Nube (5f)
Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?

- Seguridad: Los datos se encriptan antes de ser almacenados en la nube (por ejemplo, usando AWS S3 con encriptación AES-256).

- Disponibilidad: Se utilizan servicios de almacenamiento en la nube con alta disponibilidad y redundancia (por ejemplo, AWS S3 o Google Cloud Storage).

- Control de Acceso: Se implementan políticas de acceso basadas en roles (IAM) para garantizar que solo usuarios autorizados puedan acceder a los datos.

¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

- SQLite: Ideal para desarrollo y pruebas debido a su simplicidad.

- PostgreSQL: Una opción robusta para entornos de producción, con soporte para grandes volúmenes de datos.

- AWS S3: Para almacenamiento en la nube, elegido por su escalabilidad y integración con otros servicios de AWS.

Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

- Migrar la base de datos a un servicio en la nube como AWS RDS o Google Cloud SQL.

- Usar AWS S3 o Google Cloud Storage para almacenar datos históricos y respaldos.

3. Seguridad y Regulación (5i)

¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

- Encriptación: Los datos se encriptan en tránsito (usando HTTPS) y en reposo (en la base de datos).

- Autenticación: Se implementa autenticación de usuarios para acceder al panel de control y la API.

- Monitorización: Se monitorean los accesos y actividades sospechosas en el sistema.

¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

GDPR: Si el software se usa en la UE, se deben cumplir normas como el consentimiento del usuario, el derecho al olvido y la protección de datos personales.

- HIPAA: Si se manejan datos de salud, se deben implementar medidas adicionales de seguridad.

- Consideraciones: Se ha diseñado el software para permitir la eliminación de datos y se han implementado medidas de encriptación y control de acceso.

Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

- Riesgos: Acceso no autorizado, pérdida de datos o manipulación de información.

- Medidas Futuras: Implementar autenticación de dos factores, encriptación de datos y auditorías de seguridad.

4. Implicación de las THD en Negocio y Planta (2e)

¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

- Ahorro de Costos: Al monitorear el consumo energético, las empresas pueden identificar áreas de desperdicio y reducir costos.

- Sostenibilidad: Ayuda a cumplir objetivos de sostenibilidad al optimizar el uso de energía.

- Automatización: Permite integrarse con sistemas de automatización para apagar dispositivos innecesarios.

¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
Alertas en Tiempo Real: Notifica sobre consumos excesivos, permitiendo acciones inmediatas.

- Análisis de Datos: Proporciona insights para tomar decisiones basadas en datos.

- Eficiencia Operativa: Optimiza el uso de recursos energéticos.

Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
Hogares: Monitoreo del consumo doméstico para reducir facturas de energía.

- Edificios Inteligentes: Gestión centralizada de la energía en edificios comerciales.

5. Mejoras en IT y OT (2f)

¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

- Interoperabilidad: Usa protocolos estándar como MQTT para conectar dispositivos IoT (OT) con sistemas de TI.

- Visualización Centralizada: Proporciona un panel de control único para monitorear y gestionar datos de ambos entornos.

¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

- Gestión de Energía: Automatización del apagado de dispositivos no críticos durante picos de consumo.

- Mantenimiento Predictivo: Uso de datos para predecir fallos en equipos industriales.

Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

- Agricultura: Monitoreo del consumo energético en sistemas de riego.

- Logística: Optimización del consumo en flotas de vehículos eléctricos.

6. Tecnologías Habilitadoras Digitales (2g)

¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

- IoT: Sensores inteligentes para recopilar datos en tiempo real.

- Cloud Computing: Almacenamiento y procesamiento en la nube para escalabilidad.

- Big Data: Análisis de grandes volúmenes de datos para generar insights.

¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

- IoT: Permite recopilar datos precisos y en tiempo real.

- Cloud Computing: Facilita el acceso remoto y la escalabilidad del sistema.

- Big Data: Mejora la capacidad de análisis y toma de decisiones.

Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

- Integrar inteligencia artificial para predecir patrones de consumo.

- Usar blockchain para garantizar la trazabilidad y seguridad de los datos.