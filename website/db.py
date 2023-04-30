import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password= '',
)

courser = database.cursor()

courser.execute('CREATE DATABASE elderco')

print('All Done!')