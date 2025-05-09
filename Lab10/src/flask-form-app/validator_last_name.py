from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class LastNameValidator(Validator):
    def __init__(self, last_name):
        self.last_name = last_name

    def is_valid(self):
        if self.last_name is None or self.last_name.strip() == "":
            return False

        return True

    def field_name(self):
        return RegisterFormFields.LAST_NAME