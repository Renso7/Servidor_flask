# app.py
from flask import Flask, request, jsonify
import requests  # Para hacer solicitudes HTTP a otros servicios

app = Flask(__name__)

# Endpoint para obtener información desde Servicio B (Express.js)
@app.route('/from_service_b', methods=['GET'])
def get_data_from_service_b():
    try:
        # Llamar al endpoint del servicio B
        response = requests.get('https://express-service-url.com/data')
        data = response.json()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para Servicio C (FastAPI) llamando a este servicio
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"service": "A", "message": "Hello from Flask!"})

# Endpoint para conectarse a Servicio D (Fastify)
@app.route('/from_service_d', methods=['GET'])
def get_data_from_service_d():
    try:
        # Llamar al endpoint del servicio D
        response = requests.get('https://fastify-service-url.com/data')
        data = response.json()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
