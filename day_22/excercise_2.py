import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
SELECT name, price FROM products;
''')

cursor.execute('''
SELECT * FROM products WHERE quantity > 50 ORDER BY price ASC;
''')

cursor.execute('''
SELECT AVG(price) FROM products;
''')

conn.commit()
conn.close()
