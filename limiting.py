import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()


cursor.execute("select rowid,* from example order by rowid desc limit 2")
for i in cursor.fetchall():
    print("REquired adta is ", i) 



connection.commit()

connection.close()