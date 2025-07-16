rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# This is a simple Rock, Paper, Scissors game in Python where the user plays against the computer.
# The computer randomly chooses rock, paper, or scissors, and the user inputs their choice.
# The game then determines the winner based on the rules of the game.

print("Welcome to Rock, Paper, Scissors!")
print ("Choose your weapon:")
print("Type 0 for Rock")
print("Type 1 for Paper")
print("Type 2 for Scissors")

import random

#User logic
user_choice = int(input("Enter your choice (0, 1, or 2): "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()

print(f"You chose: {user_choice}")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

# Computer logic
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

print("Thanks for playing Rock, Paper, Scissors!")
# End of the Rock, Paper, Scissors game