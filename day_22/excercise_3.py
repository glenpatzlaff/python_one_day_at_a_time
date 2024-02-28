import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE products SET price = price * 1.1;
''')

cursor.execute('''
DELETE FROM products WHERE quantity < 30;
''')

conn.commit()
conn.close()
