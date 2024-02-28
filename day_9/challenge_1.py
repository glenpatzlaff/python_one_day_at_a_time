def format_products(products):
    print(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
    for product in products:
        print(f"{product['name']:<20} {product['quantity']:<10} ${product['price']:<10.2f}")

products = [
    {"name": "Apples", "quantity": 5, "price": 0.99},
    {"name": "Oranges", "quantity": 3, "price": 1.25},
    {"name": "Bananas", "quantity": 4, "price": 0.50}
]

format_products(products)
