from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, how are you?'

#Get list of product
@app.route('/products')
def get_products():
    #connect DB
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="123456",
        database="ProductManagement"
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM tblProduct")
    row_header=[x[0] for x in cursor.description]
    products = cursor.fetchall()
    json_data=[]
    for product in products:
        json_data.append(dict(zip(row_header,product)))
    cursor.close()
    return json.dumps(json_data)

@app.route('/initdb')
def initdb():
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="123456"
    )
    cursor = database.cursor()
    cursor.execute("DROP DATABASE IF EXISTS ProductManagement")
    cursor.execute("CREATE DATABASE ProductManagement")
    cursor.close()
    return 'init Database'

@app.route('/init_tables')
def init_tables():
    database = mysql.connector.connect(
        host="mysql-flask-app-container",
        user="root",
        password="123456",
        database="ProductManagement"
    )
    cursor = database.cursor()

    cursor.execute("DROP TABLE IF EXISTS tblProduct")
    cursor.execute("""CREATE TABLE tblProduct"""
    """(id INT PRIMARY KEY AUTO_INCREMENT,"""
    """name VARCHAR(255),"""
    """description VARCHAR(255))""")
    cursor.close()
    return "init_tables"

"""
INSERT INTO tblProduct(name, description)
VALUE ('Macbook Pro M1', 'Please buy'),
('Iphone 13 Promax', 'Please buy now');
"""