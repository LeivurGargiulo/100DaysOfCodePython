# Rock, Paper, Scissors Game
# This is a simple implementation of the Rock, Paper, Scissors game.
# This game is for two players.
# The players will input their choices and the program will determine the winner.

name1 = input("Enter Player 1's name: ")
name2 = input("Enter Player 2's name: ")

player1 = input(f"{name1}, please enter your choice (rock, paper, scissors): ").lower()
player2 = input(f"{name2}, please enter your choice (rock, paper, scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print(f"{name1} wins!")
else:
    print(f"{name2} wins!")
