import json
import math

# BankAccount class

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
        self.loan_balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print("Deposited successfully....")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ${amount}")
            print("Withdrawn successfully....")
        else:
            print("Insufficient funds for withdrawal....")

    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def apply_for_loan(self, amount, interest_rate, term_years):
        loan_amount = amount * math.pow(1 + interest_rate, term_years)
        self.loan_balance += loan_amount
        self.balance += loan_amount
        self.transaction_history.append(
            f"Loan applied for ${loan_amount:.2f} (Principal: ${amount}, Interest Rate: {interest_rate}, Term: {term_years} years)"
        )
        print("Loan approved! Total balance updated.")

    def view_loan_balance(self):
        print(f"Loan balance: ${self.loan_balance:.2f}")


# BankingSystem class

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = account
        print(f"Account created successfully: Account number {account_number}")

    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found....")
            return None

#File operations
 
    def save_to_file(self, filename):
        with open(filename, "w") as file:
            data = {acc: acc_obj.__dict__ for acc, acc_obj in self.accounts.items()}
            json.dump(data, file)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for acc, acc_data in data.items():
                    account = BankAccount(
                        acc_data["account_number"],
                        acc_data["account_holder"],
                        acc_data["balance"]
                    )
                    account.transaction_history = acc_data["transaction_history"]
                    account.loan_balance = acc_data["loan_balance"]
                    self.accounts[int(acc)] = account
            print(f"Data loaded successfully from {filename}")
        except FileNotFoundError:
            print("File does not exist....")


# Implement Menu system

def main():
    database = BankingSystem()
    print("....Welcome to the Advanced Banking System....")

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Apply for Loan")
        print("5. View Account Balance")
        print("6. View Transaction History")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("9. Exit\n")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            account_holder = input("Enter account holder name: ")
            database.create_account(account_holder)

        elif option == 2:
            account_number = int(input("Enter account number: "))
            account = database.find_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

        elif option == 3:
            account_number = int(input("Enter account number: "))
            account = database.find_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

        elif option == 4:
            account_number = int(input("Enter account number: "))
            account = database.find_account(account_number)
            if account:
                amount = float(input("Enter loan amount: "))
                interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
                term_years = int(input("Enter loan term in years: "))
                account.apply_for_loan(amount, interest_rate, term_years)

        elif option == 5:
            account_number = int(input("Enter account number: "))
            account = database.find_account(account_number)
            if account:
                account.view_balance()

        elif option == 6:
            account_number = int(input("Enter account number: "))
            account = database.find_account(account_number)
            if account:
                account.view_transaction_history()

        elif option == 7:
            filename = input("Enter filename to save: ")
            database.save_to_file(filename)

        elif option == 8:
            filename = input("Enter filename to load: ")
            database.load_from_file(filename)

        elif option == 9:
            print("Exiting.... Goodbye!")
            break

        else:
            print("Invalid option.... Please try again....")


main()
