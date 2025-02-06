import sqlite3
import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import bcrypt
from datetime import datetime
import random

# Configuración de la base de datos
def init_db():
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS consumption (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            consumption REAL NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Función para agregar datos de consumo
def add_consumption_data(timestamp, consumption):
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO consumption (timestamp, consumption) VALUES (?, ?)",
        (timestamp, consumption),
    )
    conn.commit()
    conn.close()

# Función para obtener datos de consumo
def get_consumption_data():
    conn = sqlite3.connect("energy_data.db")
    df = pd.read_sql_query("SELECT * FROM consumption", conn)
    conn.close()
    return df

# Función para registrar un usuario
def register_user(username, password):
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )
    conn.commit()
    conn.close()

# Función para autenticar un usuario
def authenticate_user(username, password):
    conn = sqlite3.connect("energy_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode("utf-8"), result[0]):
        return True
    return False

# Simulación de datos de sensores IoT
def simulate_sensor_data():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    consumption = round(random.uniform(100, 200), 2)  # Simula consumo entre 100 y 200 kWh
    add_consumption_data(timestamp, consumption)

# Inicializar la base de datos
init_db()

# Registrar un usuario de prueba (solo una vez)
# register_user("admin", "1234")

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout del panel de control
app.layout = html.Div(
    children=[
        html.H1("EnergyWatch - Monitoreo de Energía en Tiempo Real"),
        dcc.Input(id="username", type="text", placeholder="Usuario"),
        dcc.Input(id="password", type="password", placeholder="Contraseña"),
        html.Button("Iniciar Sesión", id="login-button"),
        html.Div(id="login-status"),
        dcc.Graph(id="consumption-graph"),
        dcc.Interval(id="interval-component", interval=5000, n_intervals=0),  # Actualizar cada 5 segundos
    ]
)

# Callback para autenticación
@app.callback(
    Output("login-status", "children"),
    Input("login-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
)
def login(n_clicks, username, password):
    if n_clicks and authenticate_user(username, password):
        return "Inicio de sesión exitoso."
    elif n_clicks:
        return "Error: Usuario o contraseña incorrectos."
    return ""

# Callback para actualizar el gráfico
@app.callback(
    Output("consumption-graph", "figure"),
    Input("interval-component", "n_intervals"),
)
def update_graph(n):
    simulate_sensor_data()  # Simular nuevos datos
    df = get_consumption_data()
    fig = px.line(df, x="timestamp", y="consumption", title="Consumo de Energía en Tiempo Real")
    return fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)