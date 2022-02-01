import sqlite3 as sql

connection= sql.connect("student.db")
cursor=connection.cursor()

def show_all():
    ...
connection.close()