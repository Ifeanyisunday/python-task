import unittest
from atm_app.bankaccountclass import BankAccount
from atm_app.accountclass import Account


class TestMyBank(unittest.TestCase):
    def test_if_no_of_customers_increase(self):
        gtb = BankAccount()
        gtb.add_account("ify", "1111")
        gtb.add_account("sunday", "2222")
        gtb.add_account("precious", "3333")
        self.assertEqual(3, gtb.get_no_of_customers())

    def test_if_deposit_of2kis2k(self):
        gtb = BankAccount()
        gtb.add_account("sunday", "2222")
        gtb.bank_deposit(1, 3000)
        self.assertEqual(3000, gtb.check_bank_balance(1))


if __name__ == '__main__':
    unittest.main()
