# Mini Game: The Forest of the Forgotten.
# A simple text-based adventure game.
print("Welcome to the Forest of the Forgotten!")
print("You wake up in a misty forest with no memory of how you got there. You only have a rusty flashlight, a coin in your pocket, and a weird sense of déjà vu. Strange sounds echo around you. Every choice might be your last… or your way out.")
choice_fork = input("You can choose to go left, right, or straight ahead.")
if choice_fork.lower() == "left":
    print("You follow a trail into the thick woods. The trees seem to whisper secrets as you pass.")
    if input("Do you want to investigate the whispers? (yes/no)") == "yes":
        print("You find a hidden path leading to a small village. The villagers seem friendly but wary.")
        if input("Do you want to ask them for help? (yes/no)") == "yes":
            print("They offer you food and shelter, but warn you about the dangers of the forest.")
        else:
            print("You decide to leave the village and continue your journey alone.")
    else:
        print("You ignore the whispers and keep walking. Suddenly, you trip over a root and fall into a hidden pit.")
        if input("Do you want to try to climb out? (yes/no)") == "yes":
            print("You manage to climb out, but now you're lost in the forest.")
        else:
            print("You decide to wait for help. Hours pass, and you realize no one is coming.")
            print("You are stuck in the pit forever.")
            print("Game Over.")
elif choice_fork.lower() == "right":
    print("You stumble upon a clearing with a strange stone altar. It looks ancient and powerful.")
    if input("Do you want to touch the altar? (yes/no)") == "yes":
        print("As you touch the altar, a blinding light engulfs you. You find yourself in a different realm.")
        if input("Do you want to explore this new realm? (yes/no)") == "yes":
            print("You discover that this realm is full of magical creatures and wonders.")
        else:
            print("You decide to return to the forest. But now, the forest seems even more mysterious.")
    else:
        print("You decide to leave the altar alone. As you turn away, you hear a voice whispering your name.")
        if input("Do you want to follow the voice? (yes/no)") == "yes":
            print("You follow the voice and find a hidden treasure chest!")
        else:
            print("You ignore the voice and continue walking. Suddenly, you are surrounded by shadows.")
            print("You are lost in the forest forever.")
            print("Game Over.")
elif choice_fork.lower() == "straight":
    print("You walk straight into a dense fog. You can barely see your own hands in front of you.")
    if input("Do you want to use your flashlight? (yes/no)") == "yes":
        print("You turn on the flashlight and see a path leading out of the fog.")
        if input("Do you want to follow the path? (yes/no)") == "yes":
            print("You find yourself at the edge of the forest, safe and sound.")
        else:
            print("You decide to stay in the fog. It gets thicker and thicker until you can't see anything.")
            print("You are lost in the fog forever.")
            print("Game Over.")
    else:
        print("You stumble around in the fog and fall into a hidden pit.")
        if input("Do you want to try to climb out? (yes/no)") == "yes":
            print("You manage to climb out, but now you're lost in the forest.")
        else:
            print("You decide to wait for help. Hours pass, and you realize no one is coming.")
            print("You are stuck in the pit forever.")
            print("Game Over.")
else:
    print("Invalid choice. You stand there confused until the forest swallows you whole.")
    print("Game Over.")
# The game ends here.   

