#Descripción del Proyecto:

- Desarrollar un software que permita a los usuarios monitorear y gestionar el consumo de energía en tiempo real en hogares, oficinas o plantas industriales. 

- El software recopilará datos de sensores IoT (como medidores de energía inteligentes) y los visualizará en un panel de control intuitivo. Además, incluirá funcionalidades como alertas de consumo excesivo, recomendaciones de ahorro energético y la posibilidad de integrarse con sistemas de automatización para optimizar el uso de energía.

- El software será desarrollado como una aplicación web con una API RESTful para facilitar la integración con otros sistemas. El código será publicado en un repositorio público bajo una licencia Open Source (por ejemplo, MIT License).


# Respuestas a las Preguntas:

# Ciclo de vida del dato (5b):

- ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

Los datos se generan a través de sensores IoT que miden el consumo de energía. Estos datos se recopilan, procesan y almacenan en una base de datos. Luego, se visualizan en el panel de control y, después de un período de tiempo definido, se archivan o eliminan para optimizar el almacenamiento.


- ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

Se implementan validaciones de datos en tiempo real para asegurar que los datos recopilados sean precisos. Además, se utilizan transacciones en la base de datos para garantizar la integridad de los datos.

- Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

Si no se trabaja con datos, se podría agregar un módulo que permita a los usuarios ingresar manualmente datos de consumo energético y generar informes basados en esos datos.

# Almacenamiento en la nube (5f):

- Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?

Se utiliza un servicio de almacenamiento en la nube como AWS S3 o Google Cloud Storage, con cifrado de datos en reposo y en tránsito. Además, se implementan copias de seguridad automáticas y redundancia para garantizar la disponibilidad.

- ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

Se consideró el almacenamiento local, pero se descartó debido a la escalabilidad y la facilidad de acceso remoto que ofrece la nube.

- Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

Si no se usa la nube, se podría migrar la base de datos y los archivos de registro a un servicio en la nube para mejorar la accesibilidad y la escalabilidad.

# Seguridad y regulación (5i):

- ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

Se implementa autenticación de usuarios, cifrado de datos y firewalls para proteger el acceso al sistema. Además, se utiliza HTTPS para asegurar las comunicaciones entre el cliente y el servidor.

- ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

Se tiene en cuenta el GDPR para garantizar la privacidad de los usuarios, especialmente en la recopilación y almacenamiento de datos personales. Se incluye una política de privacidad clara y opciones para que los usuarios gestionen sus datos.

- Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

Si no se implementan medidas de seguridad, los riesgos incluyen el acceso no autorizado a datos sensibles y la manipulación de datos. En futuras versiones, se podrían agregar autenticación de dos factores y auditorías de seguridad.


# Implicación de las THD en negocio y planta (2e):

- ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

El software permitiría a las empresas reducir costos energéticos y mejorar la eficiencia operativa. En una planta industrial, podría integrarse con sistemas SCADA para optimizar el uso de energía en tiempo real.

- ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

La solución podría mejorar la toma de decisiones al proporcionar datos precisos sobre el consumo energético y sugerir acciones correctivas.

- Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

El software también podría aplicarse en hogares inteligentes o edificios comerciales para gestionar el consumo de energía.

Mejoras en IT y OT (2f):

- ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

El software facilitaría la integración entre los sistemas de TI (como bases de datos y paneles de control) y los sistemas de OT (como sensores y medidores de energía) mediante APIs estándar.

- ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

Procesos como la gestión de energía en plantas industriales o la optimización del consumo en edificios inteligentes podrían automatizarse, reduciendo la intervención manual.

- Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Si no aplica a IT u OT, se podría adaptar para gestionar otros recursos, como el consumo de agua o la temperatura en sistemas de climatización.

Tecnologías Habilitadoras Digitales (2g):

- ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

Se utilizan IoT para la recopilación de datos, cloud computing para el almacenamiento y procesamiento, y big data para el análisis de patrones de consumo.

- ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

Estas tecnologías permiten un monitoreo en tiempo real, escalabilidad y la capacidad de procesar grandes volúmenes de datos para generar insights útiles.

- Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

Si no se han utilizado THD, se podrían integrar tecnologías como machine learning para predecir patrones de consumo y blockchain para garantizar la transparencia en la gestión de datos.
