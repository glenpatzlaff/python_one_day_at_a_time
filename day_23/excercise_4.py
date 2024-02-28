import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df_orders = pd.DataFrame({
    'OrderID': ['A001', 'A002', 'A003'],
    'CustomerID': [1, 2, 1],
    'Product': ['Book', 'Pen', 'Notebook']
})

df_merged = pd.merge(df_orders, df_customers, on='CustomerID')
orders_count = df_merged['Name'].value_counts()

print(df_merged)
print(orders_count)
