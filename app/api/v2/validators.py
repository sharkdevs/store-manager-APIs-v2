import re
from flask import jsonify

"""Check whether password is valid"""


def password_validator(password):
    if re.match(
        r'^(?=.{6,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).*',
            password):
        return True


"""Check whether the email is valid"""


def mail_validator(email):
    if re.match(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]', email.lower()):
        return True



"""Check if a field is empty"""


def is_empty(field_list):
    empty = [field for field in field_list if field ==
             "" or field.isspace() or field.isdigit()]
    for field in field_list:
        field.strip()
    if empty != []:
        return True


def is_int(field_list):
    empty = [field for field in field_list if field ==
             "" or not field.isdigit()]
    for field in field_list:
        field.strip()
    if empty != []:
        return False
