# Naruszona zasada LSP
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance = amount

class RegularAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            raise Exception('Insufficient funds')


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount >= 100: # Minimum balance must be 100
            self.set_balance(self.get_balance() - amount)
        else:
            raise Exception("Minimum balance for savings account is 100")



def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    try:
        account.deposit(deposit_amount)
        account.withdraw(withdraw_amount)
        print(f"Balance after transaction: {account.get_balance()}")
    except Exception as e:
        print(f"Transaction failed: {e}")


# Usage
# regular_account = BankAccount()

regular_account = RegularAccount()
savings_account = SavingsAccount()


perform_transaction(regular_account, 500, 200)  # Works
perform_transaction(savings_account, 500, 450)  # Exception!

