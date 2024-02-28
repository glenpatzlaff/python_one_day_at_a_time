class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, transaction_fee=1.0):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if self.balance - (amount + self.transaction_fee) >= 0:
            super().withdraw(amount)
            self.balance -= self.transaction_fee
            print(f"${self.transaction_fee:.2f} transaction fee applied.")
        else:
            print("Insufficient balance for withdrawal and transaction fee.")


# Creating account instances
savings = SavingsAccount("001", 1000)
checking = CheckingAccount("002", 500)

# Depositing and withdrawing
savings.deposit(500)
checking.withdraw(100)

# Adding interest to savings and displaying balances
savings.add_interest()
savings.display_balance()
checking.display_balance()
