# Guess the Number Game
# This is a simple number guessing game where the user has to guess a number between 1 and 100. The program provides feedback on whether the guess is too high or too low.
# The game continues until the user guesses the correct number or runs out of attemps.
# The user can also choose to play again after finishing a game.
# The game keeps track of the number of attempts made by the user to guess the number.

# The game is designed to be user-friendly and provides clear instructions on how to play.
# The game is implemented in Python and uses the random module to generate a random number.
# The game is designed to be run in a terminal or command line interface.

import random
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is?")
print("You have 10 attempts to guess the number.")
print("If you want to quit the game, type 'q' at any time.")

secret_number = random.randint(1, 101)
attempts = 0
max_attempts = 10
hasGuessed = False
while attempts < max_attempts and not hasGuessed:
    guess = input("Enter your guess (or 'q' to quit): ")
    if guess.lower() == 'q':
        print("Thanks for playing!")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        hasGuessed = True

if not hasGuessed:
    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
    print("Thanks for playing!")