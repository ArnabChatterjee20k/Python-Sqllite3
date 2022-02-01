import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()

# sorting elements.Default is ascending(asc)
cursor.execute("select * from example order by first_name desc")
print(cursor.fetchall())
connection.commit()

connection.close()
