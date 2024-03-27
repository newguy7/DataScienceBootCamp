'''
Create a regular expression pattern to match Social Security Numbers. 
SSNs in the United States are typically in the format "XXX-XX-XXXX", where X represents a digit.
'''

import re

# user_input = input("Please enter your social security number(XXX-XX-XXXX): ")

# ssn = '^\d{3}-\d{2}-\d{4}$'
# match = re.search(ssn,user_input)

# if match:
#     print("SSN is valid")
# else:
#     print("Invalid SSN")


'''
Create a regular expression pattern to match file names 
with a specific extension, such as ".txt" or ".csv".
'''

# file_name = r'\.txt|\.csv$'
# match = re.search(file_name,'hello.csv')
# if match:
#     print("valid file extension used")
# else:
#     print("incorrect file")


'''
Write a regular expression pattern to match email addresses. 
Remember that email addresses typically consist of a local part 
followed by the "@" symbol and then the domain part.
'''

# user_email = input("Enter your email address: ")

# email_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.]+\.[A-Z|a-z]{2,3}$'
# match = re.search(email_exp,user_email)

# if match:
#     print(user_email)
# else:
#     print("Invalid email")


'''
Write a Python function that extracts all URLs from a file using regular expressions. 
The function should take file name and return a list of all URLs found in the file. 
Assume, there is a file which contains multiple URLs in different places. 
Use file handling to read from file. Use findall method.
 
Sample Content: 
Visit my website at https://www.example.com. 
You can also check out https://www.example.org for more information.
'''

url_exp = r'(https?://w{3}\.[A-Za-z0-9-]+\.[A-Za-z]{2,5})'

def extract_url(url_file):

    with open(url_file, 'r') as file1:
        lines = file1.readlines()

        for line in lines:
            
            print(line.strip())
            url_match = re.findall(url_exp,line.strip())

            if url_match:
                print("Valid URL:",url_match[0],'\n')
            else:
                print("Invalid URL:")

extract_url('url_file.txt')