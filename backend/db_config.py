import mysql.connector

def connect():
    return mysql.connector.connect(
        host="php.scweb.ca",
        user="rpatel5",
        password="z66zaz66za",
        database="rpatel5"
    )