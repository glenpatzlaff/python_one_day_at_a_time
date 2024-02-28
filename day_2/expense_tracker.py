expense1 = float(input("Enter the first expense: "))
expense2 = float(input("Enter the second expense: "))
expense3 = float(input("Enter the third expense: "))

expenses = [expense1, expense2, expense3]

total_expenses = sum(expenses)

print("Total expenses: $", total_expenses)
