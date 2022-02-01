import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()


cursor.execute("drop table example")

#No table is present now so it will show us error
for i in cursor.fetchall():
    print("REquired adta is ", i)  # printing data with rowid




connection.commit()

connection.close()