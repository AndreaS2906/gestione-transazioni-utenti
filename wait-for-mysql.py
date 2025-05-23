# wait-for-mysql.py
import time
import mysql.connector
from mysql.connector import Error

while True:
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="superpassword",
            database="mydatabase"
        )
        if conn.is_connected():
            print("MySQL is ready.")
            break
    except Error:
        print("Waiting for MySQL...")
        time.sleep(2)
