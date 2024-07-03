from atm_app.accountclass import Account


class BankAccount:
    def __init__(self):
        self.no_of_customers = 0
        self.accounts = []

    def add_account(self, name, pin):
        account_instance = Account(name, pin, self.generate_acct_no())
        self.accounts.append(account_instance)
        self.no_of_customers += 1

    def get_no_of_customers(self):
        return self.no_of_customers

    def generate_acct_no(self):
        self.get_no_of_customers() + 1

    def bank_deposit(self, acct_no, amount):
        self.find_account(acct_no).deposit(amount)

    def check_bank_balance(self, acct_no):
        get_account_balance = self.find_account(acct_no)
        return get_account_balance.get_balance()

    def find_account(self, acct_no) -> Account:
        for account in self.accounts:
            account_is_found = acct_no == account.get_account_number()
            if account_is_found:
                return account

    def __str__(self):
        return f"{self.no_of_customers} {len(self.accounts)}"
