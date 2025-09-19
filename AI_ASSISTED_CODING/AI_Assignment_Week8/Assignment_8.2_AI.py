class BankAccount:  
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")
# Dynamic demo
if __name__ == "__main__":
    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(name, initial_balance)
    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

