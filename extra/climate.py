# Weather Advisor
# This program advises the user about what clothes to wear according to the current temperature.
print("Welcome to the Weather Advisor.")
temperature = int(input("Please enter the current temperature in Celsius degrees: "))
if temperature < 0:
    print("It's very cold. I recommend wearing a coat, gloves, and scarf.")
elif temperature < 20:
    print("The temperature is cool. I recommend wearing a sweater or light jacket.")
elif temperature < 30:
    print("The temperature is warm. I recommend wearing a t-shirt and shorts.")
else:
    print("It's very hot. I recommend wearing light clothing and sunscreen.")
# End of program