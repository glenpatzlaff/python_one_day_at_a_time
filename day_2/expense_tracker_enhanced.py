expenses = []

while True:
    expense = input("Enter an expense or press enter to finish: ")
    if expense == "":
        break
    expenses.append(float(expense))

total_expenses = sum(expenses)

print("Total expenses: $", total_expenses)
