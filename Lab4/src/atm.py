class InvalidPinException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass

class ATM:

    def __init__(self):
        self.users = {
            1234: 1000.0,
            1111: 1500.0,
            2222: 2000.0,
            3333: 500.0,
        }

    def check_balance(self, pin: int) -> float:
        if pin not in self.users:
            raise InvalidPinException
        return self.users[pin]

    def deposit(self, pin: int, amount: float) -> float:
        if pin not in self.users:
            raise InvalidPinException
        return self.users[pin] + amount

    def withdraw(self, pin: int, amount: float) -> float:
        if pin not in self.users:
            raise InvalidPinException

        if amount > self.users[pin]:
            raise InsufficientFundsException

        return self.users[pin] - amount
