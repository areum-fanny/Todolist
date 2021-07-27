import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)",
            ('Laundry', '2021-07-30T15:51')
            )

connection.commit()
connection.close()