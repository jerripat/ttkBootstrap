import sqlite3


conn = sqlite3.connect('presidents.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO Presidents (id, name, inauguration_date, inaugYear,endDate,vice_president) VALUES (?,?,?,?,?,?)",('Joe Biden', 'January 20', '2021', 'January 20', '2025', 'Kamala Harris'))
#result = cursor.execute("SELECT * FROM Presidents")
#for row in result:
#    print(row)



print("Successful insertion")
