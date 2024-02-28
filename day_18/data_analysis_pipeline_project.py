from functools import reduce

sales_data = [
    {"product_name": "Laptop", "category": "Electronics", "quantity_sold": 3, "price_per_item": 800},
    {"product_name": "Mouse", "category": "Electronics", "quantity_sold": 10, "price_per_item": 20},
    {"product_name": "Desk Chair", "category": "Furniture", "quantity_sold": 5, "price_per_item": 120},
    {"product_name": "Notebook", "category": "Stationery", "quantity_sold": 22, "price_per_item": 3},
    # Add more items as needed
]

def add_total_sale(transaction):
    transaction["total_sale"] = transaction["quantity_sold"] * transaction["price_per_item"]
    return transaction

transformed_data = list(map(add_total_sale, sales_data))
high_value_transactions = list(filter(lambda x: x["total_sale"] > 100, transformed_data))
total_high_value_sales = reduce(lambda acc, x: acc + x["total_sale"], high_value_transactions, 0)

print(f"Total sales from high-value transactions: ${total_high_value_sales}")
