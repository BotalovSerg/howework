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
    # connection.close()
except Error as e:
    print(f"Error {e}")



with open('data.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE users ({header[0]} varchar(25), {header[1]} INT)")
    for row in reader:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s,%s)", row)
    connection.commit()

    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    result = cursor.fetchall()

    print(result)

    # for q in result:
    #     print(q)

connection.close()
