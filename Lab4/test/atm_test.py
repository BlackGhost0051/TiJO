import unittest

from Lab4.src.atm import ATM, InvalidPinException, InsufficientFundsException


class ATMTestCase(unittest.TestCase):

    def test_pin_in_no_correct(self):
        pin = 9999
        atm = ATM()

        self.assertRaises(InvalidPinException, atm.check_balance, pin)


    def test_check_balance(self):
        atm = ATM()
        pin = 1111

        self.assertEqual(atm.check_balance(pin), 1500.0)

    def test_deposit(self):
        atm = ATM()
        pin = 1111

        self.assertEqual(atm.deposit(pin, 500.0), 2000.0)

    def test_deposit_pin_in_no_correct(self):
        pin = 9999
        atm = ATM()

        self.assertRaises(InvalidPinException, atm.deposit, pin, 500.0)

    def test_withdraw(self):
        atm = ATM()
        pin = 1111

        self.assertEqual(atm.withdraw(pin, 500.0), 1000.0)

    def test_withdraw_incorrect(self):
        atm = ATM()
        pin = 1111

        self.assertRaises(InsufficientFundsException, atm.withdraw, pin, 3000.0)

    def test_withdraw_pin_in_no_correct(self):
        pin = 9999
        atm = ATM()

        self.assertRaises(InvalidPinException, atm.withdraw, pin, 100.0)

if __name__ == '__main__':
    unittest.main()