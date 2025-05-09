from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel


    def is_valid(self):
        if len(self.pesel) != 11:
            return False

        multipliers = [1, 3, 7, 9]
        sum_ = 0


        for i in range(10):
            sum_ += int(self.pesel[i]) * multipliers[i % 4]

        modulo = sum_ % 10
        last_digit = int(self.pesel[10])

        return last_digit == (10 - modulo) % 10





    def field_name(self):
        return RegisterFormFields.PESEL