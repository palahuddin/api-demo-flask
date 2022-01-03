from flask import Flask, url_for, render_template, jsonify, request
import json
import mysql.connector
import logging
import sys
from datetime import datetime
import pytz
app = Flask(__name__)


@app.route('/')
def index():
    return {"not found": "404"}


def logger(*fn):
    tzjakarta = datetime.now(pytz.timezone('ASIA/Jakarta'))
    data = sys.stdout
    with open('out.log', 'a') as f:
        sys.stdout = f
        print(tzjakarta,"--",*fn)
        sys.stdout = data

def mysql_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="flask",
        password="password")
    db_Info = connection.get_server_info()
    logger("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    logger ("You're connected to database: ", record)
    return connection


def insert_data():
    users = request.get_json(force=True)
    data = json.loads(json.dumps(users))
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (data['nama'], data['alamat'])
    db =  mysql_db()
    mycursor = db.cursor()
    mycursor.execute(sql, val)
    db.commit()
    logger(mycursor.statement)
    logger(mycursor.rowcount, "record inserted.")
    mycursor.close()
    return users

@app.route('/me', methods=['POST'])
def me_api():
    return insert_data()
