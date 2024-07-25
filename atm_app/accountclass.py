class Account:
    def __init__(self, account_name, pin, account_number):
        self.account_name = account_name
        self.pin = pin
        self.account_number = account_number
        self.balance = 0

    def get_account_name(self):
        return self.account_name

    def get_pin(self):
        return self.pin

    def get_account_number(self):
        return self.account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.account_name} {self.balance}"

