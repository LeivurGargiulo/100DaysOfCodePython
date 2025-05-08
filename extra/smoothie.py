# Smoothie Maker
# This program is a simple smoothie maker that takes user input for ingredients and blends them together.
print("Welcome to the Smoothie Maker!")
print("Let's make a delicious smoothie.")
banana = input("Do you want to add banana? (yes/no)")
strawberry = input("Do you want to add strawberry? (yes/no)")
protein_powder = input("Do you want to add protein powder? (yes/no)")
milk = input("Do you want to add milk? (yes/no)")
ice = input("Do you want to add ice? (yes/no)")
sweetener = input("Do you want to add sweetener? (yes/no)")
print("Great! Let's blend your smoothie.")
if banana.lower() == "yes":
    print("Adding banana...")
else:
    print("No banana added.")    
if strawberry.lower() == "yes":
    print("Adding strawberry...")
else:
    print("No strawberry added.")
if protein_powder.lower() == "yes":
    print("Adding protein powder...")
else:
    print("No protein powder added.")
if milk.lower() == "yes":
    print("Adding milk...")
else:
    print("No milk added.")
if ice.lower() == "yes":
    print("Adding ice...")
else:   
    print("No ice added.")
if sweetener.lower() == "yes":
    print("Adding sweetener...")
else:
    print("No sweetener added.")
print("Blending your smoothie...")
print("Your smoothie is ready!")
print("Your smoothie contains:")
if banana.lower() == "yes":
    print("- Banana")
if strawberry.lower() == "yes":
    print("- Strawberry")
if protein_powder.lower() == "yes":
    print("- Protein Powder")
if milk.lower() == "yes":
    print("- Milk")
if ice.lower() == "yes":
    print("- Ice")
if sweetener.lower() == "yes":
    print("- Sweetener")
print("Your smoothie is ready! Enjoy!") 
print("Thank you for using the Smoothie Maker!")
