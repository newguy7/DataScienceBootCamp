'''
Write a program, ask user to input two numbers and print the result, try to catch ZeroDivisionError. 
'''
# def div_func(x,y):
#     try:        
#         res = x/y
#         print(res)
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")

# # Asking for user input
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter second number: "))

# # Calling the function
# div_func(num1,num2)

'''
Write a Python function read_file(filename)
that takes a filename as input and reads the contents of the file. 
Your function should handle potential exceptions that might occur during the file reading process.
'''

def read_file(filename):
    try:
        with open(filename,'r') as rf:
            lines = rf.readlines()

            for line in lines:
                print(line.strip())

            # #throw error
            # rf.write("Hello\n")

    except FileNotFoundError:
        
        print(f"{filename} not found.")    

file_name = input("Please provide the filename: ")

read_file(file_name)