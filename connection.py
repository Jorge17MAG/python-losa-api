import mysql.connector
from mysql.connector import Error

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="db_losadeportiva",
            user="root",
            password="123456"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return connection

def close_db_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada")
