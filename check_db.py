import sqlite3

conn = sqlite3.connect('packets.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM packets ORDER BY id DESC LIMIT 10'):
    print(row)

conn.close()
