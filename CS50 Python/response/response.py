from validator_collection import validators, checkers, errors

user = input("enter your email address: ")
try:
    ValidEmail = validators.email(user)
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
except errors.EmptyValueError:
    print("Invalid")

