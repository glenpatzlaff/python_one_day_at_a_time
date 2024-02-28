import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER, order_date TEXT, quantity INTEGER);
''')

cursor.execute('''
INSERT INTO orders (product_id, order_date, quantity) VALUES (1, '2020-01-01', 50);
''')

cursor.execute('''
SELECT products.name, SUM(orders.quantity) AS total_ordered FROM orders JOIN products ON orders.product_id = products.id GROUP BY product_id ORDER BY total_ordered DESC;
''')

cursor.execute('''
UPDATE products SET price = price * 0.95 WHERE id IN (SELECT product_id FROM orders GROUP BY product_id HAVING SUM(quantity) > 100);
''')

conn.commit()
conn.close()
