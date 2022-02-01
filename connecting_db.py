import sqlite3 as sql
#creating a connection

# connection=sql.connect(":memory:")
# #here it will not create a file.It allow us to use a database in memory and as soon as the program execution over the database disappers.

connection=sql.connect("examples.db")#this will connect to database present in the directory.If that doesnot exist then it will create a new one.

connection.close()
