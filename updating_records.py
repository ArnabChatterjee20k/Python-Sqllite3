import sqlite3 as sql

connection = sql.connect("examples.db")


cursor = connection.cursor()


cursor.execute(
    """

    update example set first_name="BITTU"where  rowid=1
"""
)

connection.commit()

connection.close()
