import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL);
''')

cursor.execute('''
INSERT INTO products (name, quantity, price) VALUES ('Product A', 100, 9.99);
''')

conn.commit()
conn.close()
