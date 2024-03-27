# program to calculate BMI

# user_weight = float(input("Enter your weight in kg: "))
# user_height = float(input("Enter your height in meter: "))

# bmi = int(user_weight/(user_height ** 2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight") 
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are Clinically obese")

# Rock, Paper, Scissor
user_choice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

for num in range(0,3):
    computer_choice = num

if user_choice == 0 and computer_choice == 1:
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print("")
elif user_choice == 0 and computer_choice == 2:
    pass

print(user_choice)
print(computer_choice)