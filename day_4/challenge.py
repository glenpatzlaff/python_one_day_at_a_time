price = float(input("Enter the price of the product: "))

if price <= 0:
    print("Invalid price")
elif price <= 100:
    print("Budget")
elif price <= 500:
    print("Mid-range")
else:
    print("Premium")
