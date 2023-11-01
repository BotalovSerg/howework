import os
import mysql.connector as mariadb
from mysql.connector import Error



print("Hello World")
print(os.environ.get("DB_USERNAME"))

try:
    connection = mariadb.connect(
        user=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB"),
        host=os.environ.get("HOST"),
        port=os.environ.get("PORT"))
    print("Connect MariaDB")
    connection.close()
except Error as e:
    print(f"Error {e}")