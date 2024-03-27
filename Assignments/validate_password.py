'''
Write a Python function validate_password(password)
that takes a password string as input and validates it based on the following criteria:

1. The password must be at least 8 characters long.
2. The password must contain at least one uppercase letter, one lowercase letter, 
one digit, and one special character (e.g., !, @, #, $, %, ^, &, *).
3. The password must not contain whitespace characters.

Your function should raise custom exceptions for different cases of invalid passwords 
and return True if the password is valid.

'''
# regular expressions
import re

def validate_password(password): 
    
    check_upper = bool(re.search(r"[A-Z]", password))
    check_lower = bool(re.search(r"[a-z]", password))
    check_digit = bool(re.search(r"\d", password))
    check_special = bool(re.search(r"[!@#$%^&*]", password))
    check_whitespace = bool(re.search(r'[\s]', password))      
    
    if (len(password) < 8):
        raise ValueError("Password must be at least 8 characters long")
    if (not check_upper):
        raise ValueError("Password does not contain a uppercase letter")
    if (not check_lower):
        raise ValueError("Password does not contain a lowercase letter")
    if (not check_digit):
        raise ValueError("Password does not contain any numbers")
    if (not check_special):
        raise ValueError("Password does not contain any special characters")
    if (check_whitespace):
        raise ValueError("Password contains whitespace")
    
    return True   

user_password = input("Enter your password: ")
try:
    if (validate_password(user_password)==True):
        print("Password is valid!")
except ValueError as ve:
    print("Error message is:", ve.args[0])