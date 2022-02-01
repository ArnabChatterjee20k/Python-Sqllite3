import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()

# to execute multiple statements
cursor.executescript(
    """delete from example where rowid=4;
                insert into example values("Jden","Asa");"""
)
cursor.execute("select * from example")
print(cursor.fetchall())
connection.commit()

connection.close()
