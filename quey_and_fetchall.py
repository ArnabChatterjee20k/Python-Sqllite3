import sqlite3 as sql
connection=sql.connect("examples.db")


cursor=connection.cursor()


cursor.execute(
"""select * from example"""
)

print(cursor.fetchmany(3))# upto 3rd row

# print(cursor.fetchall())# all rows will be printed

# cursor.fetchone()#fetchone() gives us 1 row at a time.By default it returns first row. We can get many all rows by using loop. Return format is list and inside it rows are present in form of tuples

# for i in range(1,10):
#     print(cursor.fetchone())
#>>>> Output
    #('Arnab', 'Chatterjee')
    # ('Arnab', 'Chatterjee')
    # ('Arnab', 'Ch')
    # ('Arnab', 'Ch')
    # ('Bittu', 'Ch')
    # ('A', 'B')
    # ('C', 'D')
    # ('E', 'F')
    # None  #None as no value is present at that row

# after using using one fetch function if we use another then it will return none

connection.commit()

connection.close()

