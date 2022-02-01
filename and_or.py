import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()


cursor.execute("select * from example order by first_name like '%A' and last not like '%s%' desc")
print(cursor.fetchall())
connection.commit()

connection.close()
