import sqlite3 as sql

connection=sql.connect("examples.db")

data=[("A","B"),
      ("C","D"),
      ("E","F")
]

cursor=connection.cursor()

cursor.executemany("insert into example values(?,?)",data)
#using a placeholder and executemany

connection.commit()

connection.close()
