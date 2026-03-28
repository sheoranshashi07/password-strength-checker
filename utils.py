import re

# Check if password contains uppercase letter
def has_uppercase(password):
    return bool(re.search("[A-Z]", password))


# Check if password contains lowercase letter
def has_lowercase(password):
    return bool(re.search("[a-z]", password))


# Check if password contains a number
def has_number(password):
    return bool(re.search("[0-9]", password))


# Check if password contains special characters
def has_special_character(password):
    return bool(re.search("[@#$%^&*!]", password))
