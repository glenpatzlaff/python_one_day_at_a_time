inventory = {}
categories = set()

def add_item(name, stock, price, category):
    inventory[name] = {"stock": stock, "price": price}
    categories.add(category)

def update_item(name, stock=None, price=None):
    if name in inventory:
        if stock is not None:
            inventory[name]["stock"] = stock
        if price is not None:
            inventory[name]["price"] = price
    else:
        print(f"Item '{name}' not found in inventory.")

def delete_item(name):
    if name in inventory:
        del inventory[name]
    else:
        print(f"Item '{name}' not found in inventory.")

def view_inventory():
    for name, details in inventory.items():
        print(f"{name}: Stock = {details['stock']}, Price = ${details['price']}")

def view_categories():
    print("Categories:", ", ".join(categories))

add_item("Laptop", 10, 999.99, "Electronics")
add_item("Coffee Mug", 50, 5.99, "Kitchenware")
update_item("Laptop", stock=8)
delete_item("Coffee Mug")
view_inventory()
view_categories()

