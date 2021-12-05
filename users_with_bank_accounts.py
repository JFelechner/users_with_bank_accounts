
class User:

    def __init__(self , name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawl(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self

class BankAccount:

    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    def display_account_info(self):
        print(f"Bank Account: {self.name}, Balance: {self.balance}")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

user1 = User("Jack")
user1.make_deposit(2000).display_user_balance()
