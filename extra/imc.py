# BMI Calculator
# This program calculates the user's BMI.
print("Welcome to the BMI calculator")
weight = int(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are healthy.")
else:
    print("You are overweight.")