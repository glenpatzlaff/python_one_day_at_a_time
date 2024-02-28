expenses = {}

while True:
    category = input("Enter the expense category or press enter to finish: ")
    if category == "":
        break
    amount = float(input(f"Enter the amount for {category}: "))
    expenses[category] = expenses.get(category, 0) + amount

    total_expenses = sum(expenses.values())

    print("Total expenses: $", total_expenses)

