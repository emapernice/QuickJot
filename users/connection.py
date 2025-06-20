import mysql.connector
from mysql.connector import Error
from config.settings import DB_CONFIG

def connect():
    try:
        database = mysql.connector.connect(**DB_CONFIG)
        cursor = database.cursor(buffered=True)
        return database, cursor
    except Error as e:
        print(f"Database connection error: {e}")
        return None, None
