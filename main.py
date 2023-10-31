import mysql.connector as mariadb
from mysql.connector import Error


connection = mariadb.connect(
    user='myuser',
    password='mypassword',
    database='mydb',
    host='localhost',
    port='3306')
    

cursor = connection.cursor()
# cursor.execute("CREATE TABLE users \
#                (name varchar(25), \
#                age INT)")
# Populate countries table  with some data
cursor.execute("INSERT INTO users (name, age) VALUES ('Serg', '37');")
connection.commit()

connection.close()