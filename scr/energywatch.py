from flask import Flask, jsonify, render_template, request
import sqlite3
import paho.mqtt.client as mqtt
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'energy_monitor.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS energy_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                consumption REAL NOT NULL
            )
        ''')
        conn.commit()

# Configuración de MQTT
MQTT_BROKER = 'broker.hivemq.com'
MQTT_TOPIC = 'energy/consumption'

def on_message(client, userdata, message):
    # Procesar datos recibidos del sensor IoT
    payload = float(message.payload.decode())
    timestamp = datetime.now().isoformat()
    save_energy_data(timestamp, payload)
    print(f"Dato recibido: {payload} kW en {timestamp}")

def save_energy_data(timestamp, consumption):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO energy_data (timestamp, consumption) VALUES (?, ?)', (timestamp, consumption))
        conn.commit()

# Iniciar cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, 1883, 60)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.loop_start()

# Rutas de la API
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/energy', methods=['GET'])
def get_energy_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT timestamp, consumption FROM energy_data ORDER BY timestamp DESC LIMIT 100')
        data = cursor.fetchall()
    return jsonify(data)

@app.route('/api/alert', methods=['POST'])
def send_alert():
    # Lógica para enviar alertas (por ejemplo, por correo electrónico)
    alert_message = request.json.get('message')
    print(f"Alerta enviada: {alert_message}")
    return jsonify({'status': 'success', 'message': 'Alerta enviada'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
