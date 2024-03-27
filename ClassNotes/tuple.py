# t1 = ('A','B')
# t2 = (5,'C',7,'D')
# t3 = t1 + t2
# print(t3)

# print(t3[::-1]) # reverse a tuple

# print(t3[1:5:3]) # starts from position 1 and prints every 3rd element after that and goes all the way to the last element

# print(t3.index('A')) # gets the index of the element in the tuple 

# Check if the user input is a number or not. Then check if it is of type integer or float

user_input = input("Please type here: ")

def check_input(input1):
    try:
        input_passed = int(input1)
        print("User input is a integer. Number = ", input_passed)
    except ValueError:
        try:
            input_passed = float(input1)
            print("User input is a float. Number = ", input_passed)
        except ValueError:
            print("The user input is not a number but a string.")
        

check_input(user_input)

