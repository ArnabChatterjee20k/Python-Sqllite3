import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()


cursor.execute("select rowid,* from example where rowid=1")
for i in cursor.fetchall():
    print("REquired adta is ", i)  # printing data with rowid


cursor.execute("select * from example where first_name like 'A%' ")

for i in cursor.fetchall():
    print(i)  # printing data with rowid

# wild card entries with like
# A% means record starting with A
# %A means record ending with A
# %A% means record with A in any position in middle
connection.commit()

connection.close()
