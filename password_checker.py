from utils import has_uppercase, has_lowercase, has_number, has_special_character

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if has_uppercase(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Moderate Password"
    else:
        return "Strong Password"


password = input("Enter your password: ")

strength = check_password_strength(password)

print("Password Strength:", strength)
