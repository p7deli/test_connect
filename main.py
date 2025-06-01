import mysql.connector as connector


db = connector.connect(
    host='localhost',
    user='admin',
    password='1234'
)


cursor = db.cursor()
cursor.execute('CREATE DATABASE Hello;')
db.commit()
db.close()