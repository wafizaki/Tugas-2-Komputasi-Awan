import time
import random
import mysql.connector
import os

db_config = {
    'user': 'root',
    'password':'adminpassword',
    'host':'database',
    'database':'farming_db',
    }

print("Sensor started... waiting for DB...")
time.sleep(10)

while True:
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        temp = round(random.uniform(25.0,35.0), 2)
        hum = round(random.uniform(60.0,90.0), 2)
        node = os.getenv('HOSTNAME', 'sensor-node')

        query = "INSERT INTO sensor_logs (node_name, temperature, humidity) VALUES (%s, %s, %s)"
        cursor.execute(query, (node, temp, hum))
        conn.commit()

        print(f"Data Sent: Temp={temp}C, Hum={hum}%")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5) # Kirim data setiap 5 detik
