import mysql.connector as mariadb
from mysql.connector import Error
import csv



try:
    connection = mariadb.connect(
        user='myuser',
        password='mypassword',
        database='mydb',
        host='localhost',
        port='3306')
    print("Connect MariaDB")    
except Error as e:
    print(f"Error {e}")        

cursor = connection.cursor()
# with open('data.csv') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     cursor.execute(f"CREATE TABLE users ({header[0]} varchar(25), {header[1]} INT)")   

#     for row in reader:
#         cursor.execute(f"INSERT INTO users (name, age) VALUES ({row[0]}, {row[1]})")
#         print(row[0], "  ", row[1])    
#         connection.commit()

# cursor = connection.cursor()
# cursor.execute("CREATE TABLE users \
#                (name varchar(25), \
#                age INT)")
# Populate countries table  with some data
u = ['Maks', 25]
cursor.execute("INSERT INTO users (name, age) VALUES (%s,%s)", u)
connection.commit()
connection.close()

