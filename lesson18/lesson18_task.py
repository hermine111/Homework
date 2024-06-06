# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return f"Balance:  {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = amount * self.interest_rate
        self.balance += interest


savings_a = SavingsAccount(11111111111, 800)
savings_a.deposit(500)
print(savings_a.get_balance())


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee=30):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_fee


checking_a = CheckingAccount(456987, 800)
checking_a.deposit(200)
checking_a.withdraw(8500)
print(checking_a.get_balance())

