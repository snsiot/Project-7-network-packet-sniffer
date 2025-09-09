import sqlite3

conn = sqlite3.connect('packets.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    src_ip TEXT,
    dst_ip TEXT,
    src_port INTEGER,
    dst_port INTEGER,
    length INTEGER,
    flags TEXT
)
''')

conn.commit()
conn.close()
print("Database and table created!")
