import os
import mysql.connector as mariadb
from flask import Flask




connection = mariadb.connect(
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB"),
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"))



app = Flask(__name__)


@app.route('/')
def status_ok():
    return "<h1>Hello, Flask</h1>"


@app.route('/health')
def health():
    return {"status": "OK"}

@app.route('/db')
def db_ok():
    json_data = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    # result = cursor.fetchall()
    # connection.close()
    row_headers=[x[0] for x in cursor.description] 
    for result in cursor:
        json_data.append(dict(zip(row_headers,result)))
    return json_data

if __name__ == '__main__':
    app.run(host='0.0.0.0')