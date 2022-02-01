import sqlite3 as sql

connection=sql.connect("examples.db")

#creating a cursor.It will act as a pointer in the database file where we want to modify the file
cursor=connection.cursor()

# executing commands to make tables
#making table by docstrings.It will allow us to work in multiple lines
cursor.execute("""
    create table example(
        first_name text,
        last text
    )
""")#here we are adding records/rows

connection.commit()#commit allow us to save the data into the database


#closing our connection
connection.close()

#sqlite3 has 5datatypes===
#NULL
# INTEGER
# REAL
# TEXT
# BLOB == to store file as it is like images,mp3 files,etc
# 
