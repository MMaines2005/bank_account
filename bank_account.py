class BankAccount:
    def __init__(self, balance=0, int_rate=0.02):
        self.balance = balance
        self.int_rate = int_rate
        # self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= amount:
            print("Insufficent Funds")
        return self
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance*self.int_rate
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount): 
        self.account.deposit(amount)
        return self

    def get_cash(self, amount):
        self.account.withdraw(amount)
        return self

    def account_info(self):
        self.account.display_account_info()

    def transfer(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.balance -= amount
        return self

michael = User("Michael pompernickle", "pompernickle@cantgetthistowork.com")
linda = User("Anna pompernickle", "annanickle@cantgetthistowork.com")
Bob = User("Guido van Rossum", "guido@python.com")
Izzy = User("Monty Python", "monty@python.com")

Izzy.make_deposit(100).make_deposit(200).make_deposit(300).get_cash(50).account_info()
linda.make_deposit(3000).make_deposit(300).account_info()
michael.account_info()