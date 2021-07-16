class BankAccount:
    def __init__(self, balance=0, int_rate=0.02):
        self.balance = balance
        self.int_rate = int_rate
        

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= amount:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(f"Your balance is: ", self.balance)
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

michael = User("Michael Luckiest", "MichaelLuck@luckville.com")
linda = User("Linda Luckiest", "lindaLuck@luckville.com")
Bob = User("Bob Ross", "BRoss@paint.com")
Izzy = User("Izzy Arts", "Izzyarts@paint.com")

Izzy.make_deposit(100).make_deposit(200).make_deposit(300).get_cash(50).account_info()
linda.make_deposit(3000).make_deposit(300).account_info()
michael.get_cash(10).account_info()