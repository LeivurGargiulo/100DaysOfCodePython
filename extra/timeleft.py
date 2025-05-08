# Remaining Life Calculator.
# This program calculates how much time the user has left to live, assuming they will die as soon as they turn 90.
print("Welcome! Let's calculate how much time you have left to live.")
print("Remember: You will die as soon as you turn 90 years old.")
name = input("What is your name?\n")
birth_year = int(input("Enter your birth year.\n"))
age = 2025 - birth_year
years_left = 90 - age
print(f"Your name is {name} and you were born in the year {birth_year}. You are {age} years old.")
print(f"You have {years_left} years left to live.")
months_left = years_left * 12
print(f"You have {months_left} months left to live.")
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left to live.")
days_left = years_left * 365
print(f"You have {days_left} days left to live.")
print("Remember to enjoy each day and live life to the fullest.")