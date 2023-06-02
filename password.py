import re

def password(pasword):

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])(?!.*\s).{8,}$"
    if re.match(pattern, pasword):
        return "Valid password"
    else:
        return "Invalid password"


pasword = input("Enter your password:  ")
print(password(pasword))


