expenses = []
income = []

def add_expense(amount, category, date):
    expenses.append({"amount": amount, "category": category, "date": date})

def add_income(amount, source, date):
    income.append({"amount": amount, "source": source, "date": date})

def calculate_balance():
    total_expenses = sum(expense["amount"] for expense in expenses)
    total_income = sum(inc["amount"] for inc in income)
    return total_income - total_expenses

def print_summary():
    print("Expenses:")
    for expense in expenses:
        print(f"{expense['date']}: {expense['category']} - ${expense['amount']}")
    print("\nIncome:")
    for inc in income:
        print(f"{inc['date']}: {inc['source']} - ${inc['amount']}")
    print(f"\nCurrent Balance: ${calculate_balance()}")

def main():
    while True:
        action = input("Choose an action - Add Expense (E), Add Income (I), View Summary (S), Quit (Q): ").upper()
        if action == "Q":
            break
        elif action == "E":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (MM/DD/YYYY): ")
            add_expense(amount, category, date)
        elif action == "I":
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            date = input("Enter date (MM/DD/YYYY): ")
            add_income(amount, source, date)
        elif action == "S":
            print_summary()
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
