class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.05

    # Constructor to initialize account holder and balance
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    # Method to deposit amount into account
    def deposit(self, amount):
        self.balance += amount

    # Method to withdraw amount from account if sufficient balance exists
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.account_holder}!")

    # Method to apply interest to the current balance
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    # Method to display account information
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance:.2f}")


# Creating two instances of BankAccount with different account holders
account_1 = BankAccount("Alice")
account_2 = BankAccount("Bob")

# Performing deposits and withdrawals on both accounts
account_1.deposit(1000)
account_1.withdraw(200)
account_1.apply_interest()

account_2.deposit(500)
account_2.withdraw(100)
account_2.apply_interest()

# Displaying the account information for each account
account_1.display_account_info()
account_2.display_account_info()
