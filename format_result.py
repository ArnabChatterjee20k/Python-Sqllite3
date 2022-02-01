import sqlite3 as sql

connection=sql.connect(r"D:\Python\web_scraping\Oneplus earphones.db")


cursor=connection.cursor()
cursor.execute(
"""select * from REVIEW"""
)
data=cursor.fetchall()

print(data)
# whole_data=dict()
# for i in data:
#     whole_data[data.index(i)+1]=i 

# print(whole_data)   

# for i in whole_data:
#     print(i,"\t",whole_data[i][0]+"\t"+whole_data[i][1])
# connection.commit()

connection.close()
