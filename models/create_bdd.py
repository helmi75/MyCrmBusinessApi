import sqlite3

conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE clients
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                email TEXT)''')

conn.commit()
conn.close()

