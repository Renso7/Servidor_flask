from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Conexión a la base de datos (PostgreSQL en Supabase o un servicio similar)
DATABASE_URL = os.environ.get('postgresql://postgres.hwuuwwjjqqpqffhfxama:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:6543/postgres')  # Configura esta variable de entorno en Render

def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
