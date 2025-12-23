import sqlite3

db = sqlite3.connect("tasks.db")
sql = db.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS todo (task TEXT, status TEXT)")

sql.execute("INSERT INTO todo VALUES ('купить молоко', 'Не сделано')")

sql.execute("SELECT * FROM todo")
print(sql.fetchall())

db.commit()

sql.execute("SELECT * FROM todo")
rows = sql.fetchall()
print("Содержимое таблицы")
for row in rows:
    print(row)

db.close()

