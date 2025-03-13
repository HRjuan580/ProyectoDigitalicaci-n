# Descripción del Proyecto:

- Desarrollar un software que permita a los usuarios monitorear y gestionar el consumo de energía en tiempo real en hogares, oficinas o plantas industriales. 

- El software recopilará datos de sensores IoT (como medidores de energía inteligentes) y los visualizará en un panel de control intuitivo. Además, incluirá funcionalidades como alertas de consumo excesivo, recomendaciones de ahorro energético y la posibilidad de integrarse con sistemas de automatización para optimizar el uso de energía.

- El software será desarrollado como una aplicación web con una API RESTful para facilitar la integración con otros sistemas. El código será publicado en un repositorio público bajo una licencia Open Source (por ejemplo, MIT License).


# Explicación del Funcionamiento del Código


1. Backend (Python - Flask)
El backend del proyecto está desarrollado en Python utilizando el framework Flask. Su función principal es recibir datos de consumo energético desde sensores IoT, almacenarlos en una base de datos y proporcionar una API RESTful para que el frontend pueda acceder a estos datos.

Componentes Principales:
Base de Datos (SQLite):

- Se utiliza SQLite para almacenar los datos de consumo energético.

- La tabla energy_data guarda:

    id: Identificador único de cada registro.

    timestamp: Fecha y hora en que se registró el consumo.

    consumption: Valor del consumo energético en kW.

2. Conexión MQTT:

- El servidor se conecta a un broker MQTT (por ejemplo, broker.hivemq.com) para recibir datos en tiempo real desde sensores IoT.

- Cuando se recibe un mensaje en el tópico energy/consumption, se procesa y almacena en la base de datos.

3. API RESTful:

- GET /api/energy: Devuelve los últimos 100 registros de consumo energético en formato JSON.

- POST /api/alert: Permite enviar alertas (por ejemplo, notificaciones por correo electrónico o SMS).

4. Inicialización de la Base de Datos:

Al iniciar la aplicación, se verifica si la tabla energy_data existe. Si no existe, se crea automáticamente.

# Flujo de Trabajo del Backend:
El servidor se conecta al broker MQTT y se suscribe al tópico energy/consumption.

Cuando llega un nuevo dato, se guarda en la base de datos con la marca de tiempo actual.

El frontend puede acceder a los datos históricos mediante la API RESTful.

5. Frontend (HTML + JavaScript + Chart.js)
El frontend es una interfaz web que muestra los datos de consumo energético en tiempo real utilizando gráficos interactivos. Se utiliza la biblioteca Chart.js para crear gráficos dinámicos.

Componentes Principales:
- Gráfico de Líneas:
    Muestra el consumo energético en tiempo real.

    El eje X representa el tiempo y el eje Y representa el consumo en kW.

- Actualización Automática:

    Cada 5 segundos, el frontend realiza una solicitud a la API (GET /api/energy) para obtener los últimos datos y actualizar el gráfico.

- Diseño Responsivo:

    La interfaz es compatible con dispositivos móviles y de escritorio.

- Flujo de Trabajo del Frontend:
    Al cargar la página, se inicializa un gráfico vacío.

    Cada 5 segundos, se realiza una solicitud a la API para obtener los últimos datos.

    Los datos se actualizan en el gráfico, mostrando el consumo energético en tiempo real.

6. Comunicación IoT (MQTT)
El proyecto utiliza el protocolo MQTT para recibir datos desde sensores IoT. MQTT es un protocolo ligero y eficiente, ideal para dispositivos con recursos limitados.

# Componentes Principales:
- Broker MQTT:

    Se utiliza un broker público (broker.hivemq.com) para recibir datos.

    En un entorno de producción, se recomienda usar un broker privado (por ejemplo, Mosquitto o AWS IoT Core).

- Tópico:

    Los sensores publican datos en el tópico energy/consumption.

    El servidor está suscrito a este tópico para recibir los datos.

- Formato de los Datos:

    Los datos se envían como un valor numérico (consumo en kW) en formato de texto.

7. Almacenamiento y Seguridad
- Almacenamiento:

    Los datos se almacenan en una base de datos SQLite para desarrollo.

    En producción, se recomienda usar una base de datos más robusta como PostgreSQL o MySQL.

- Seguridad:

    El código incluye un mecanismo básico para enviar alertas.

    En un entorno real, se deben implementar medidas adicionales como autenticación de usuarios y encriptación de datos.

# Instrucciones de Uso
- Requisitos:

    Python 3.x

    Librerías requeridas: Flask, paho-mqtt, sqlite3

    Instalar dependencias: pip install -r requirements.txt

- Ejecución:

    Iniciar el servidor: python main.py

    Acceder al panel de control: Abrir http://localhost:5000 en un navegador.

- Configuración MQTT:

    Modificar el broker y tópico MQTT en el código si es necesario.

- Despliegue en Producción:

    Usar un servidor WSGI (por ejemplo, Gunicorn) para desplegar la aplicación.

    Configurar un broker MQTT privado.


# Licencia
Este proyecto está bajo la licencia de MIT. Consulta LICENCE para mas detalles



# Preguntas a responder

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


