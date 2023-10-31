print("Hello World")


import mysql.connector as mariadb
from mysql.connector import Error

try:
    connection = mariadb.connect(
        user='myuser',
        password='mypassword',
        database='mydb',
        host='db',
        port='3306')
    print("Connect MariaDB")
    connection.close()
except Error as e:
    print(f"Error {e}")