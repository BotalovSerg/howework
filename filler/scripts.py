import os
import mysql.connector as mariadb
from mysql.connector import Error
import csv


print("Hello World")

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



with open('data.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Headers :', header)
    for row in reader:
        print(row)
