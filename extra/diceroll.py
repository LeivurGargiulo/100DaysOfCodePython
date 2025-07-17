# This program asks the user to input a number of dice to roll and then simulates rolling that many six-sided dice.
import random

print("Welcome to the Dice Roller!")
print("How many dice would you like to roll?")
number_of_dice = input("Enter a number: ")
for i in range(int(number_of_dice)):
    roll = random.randint(1, 6)
    print(f"Roll {i + 1}: {roll}")
print("Thank you for using the Dice Roller!")
# End of the dice rolling simulation.