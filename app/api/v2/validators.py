import re
from flask import jsonify
from app.api.v2.database import Db


"""Check whether password is valid"""
def password_validator(password):
    if re.match(r'[A-Za-z0-9!@£$%^&*()_+={}?:~[+]{6,}', password):
        return True

"""Check whether the email is valid"""
def mail_validator(email):
    if re.match(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]', email.lower()):
        return True

"""Check if the email is registered"""
def filter_item_detail(email, user_list):
    user = [user for user in user_list if user['email'] == email]
    return user

"""Check if a field is empty"""
def is_empty(field_list):
    empty = [field for field in field_list if field == "" or field.isspace()]
    if empty != []:
        return True

def validate_registration(username, email, password, role, users_list):
    err = []
    if password_validator(password) != True:
        err.append(
            "Password must contain A capital letter, a small letter, a number and a special character")
    if mail_validator(email) != True:
        err.append("Wrong email address entered")
    if username == "" or role == "":
        err.append("You cannot insert empty data")
    if not filter_item_detail(email, users_list):
        pass
    else:
        err.append("{} is already taken. Try another email".format(email))
    return err

def validate_login(email, password, users_list):
    error = []
    # check whether the iser is registered
    registered_user = filter_item_detail(email, users_list)

    if is_empty([email, password]):
        error.append("Please enter data in the fields")
    if error == [] and mail_validator(email) != True:
        error.append("Invalid email address")

    if error == [] and not registered_user:
        error.append("{} is not a registered user".format(email))

    if error == [] and registered_user[0]['password'] != password:  # check user password
        error.append("Incorrect Password")

    return error
