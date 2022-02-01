import sqlite3 as sql

connection=sql.connect("examples.db")


cursor=connection.cursor()

#inserting recors
cursor.execute(
"""
insert into example values("Bittu","Ch") 
"""#inserted one row to the table example
)
print("Done")
connection.commit()

connection.close()

#The no.of times we will run this code everytime it will insert the rows/records into the example table