# __Challenge__

# Create account class with two attributes balance and account no.
# Create method for Debit, Credit, and printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def print_balance(self):
        print("Your balance is", self.balance)
        
    def debit(self, debit_amount):
        self.balance -= debit_amount 
        print(f"{debit_amount} debited..")
        self.print_balance()

    def credit(self, credit_amount):
        self.balance += credit_amount 
        print(f"{credit_amount} credited..")
        self.print_balance()

customer1 = Account(10000, 9870)
customer1.print_balance()

customer1.debit(2000)
customer1.credit(5000)