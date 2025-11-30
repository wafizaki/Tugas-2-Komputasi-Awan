from flask import Flask, render_template
import mysql.connector
import os
import socket

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        user='root', password='adminpassword',
        host='database', database='farming_db'
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Ambil 10 data terakhir
        cursor.execute("SELECT * FROM sensor_logs ORDER BY timestamp DESC LIMIT 10")
        logs = cursor.fetchall()
        conn.close()
    except:
        logs = []

    # Info container ini (biar kelihatan Load Balancingnya)
    server_info = {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname())
    }
    
    return render_template('index.html', logs=logs, server=server_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
