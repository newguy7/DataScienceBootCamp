'''
Write a Python function validate_email(email) that takes an email address string as input 
and validates it based on the following criteria:
The email address must have a valid format, i.e., it should have an "@" symbol followed by a domain name.
The domain name must have at least one dot.
The email address must not contain whitespace characters.
Your function should raise custom exceptions for different cases of invalid email addresses 
and return True if the email address is valid.

'''

def validate_email(email):
  
    if (not '@' in email):
        raise ValueError("Email must contain @ symbol")
    
    # getting the domain name
    first_part, domain_part = email.split('@')

    if (not first_part):
        raise ValueError("Email must contain email address before @ symbol")
    
    if (not domain_part):
        raise ValueError("Email must contain domain name after @ symbol")
    
    if (not '.' in email):
        raise ValueError("Email must contain at least one dot")
    
    if (' ' in email):
        raise ValueError("Email contains whitespace")
    
    return True

user_email = input("Enter your email address: ")
try:
    if (validate_email(user_email)==True):
        print("Email address is valid!")
except ValueError as ve:
    print("Error message is:", ve.args[0])