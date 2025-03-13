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


