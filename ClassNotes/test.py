
# program to calculate BMI

user_weight = float(input("Enter your weight: "))
user_height = int(input("Enter your height: "))

bmi = user_weight/(user_height ** 2)

if bmi < 18.5:
    print("Your are underweight")
elif bmi < 25:
    print("You are normal weight") 
elif bmi < 30:
    print("You are over weight")
elif bmi < 35:
    print("You are obese")
elif bmi > 35:
    print("Clinically obese")

