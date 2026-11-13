# Name: Rishi Scaro, Date: 10/15/2026, Description: This program is a guessing game where the user has to guess a randomly generated number correctly. 


import random

print("Welcome to the higher/lower game!")

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

while lower >= upper:
    print("Invalid bounds. Try again.")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

number = random.randint(lower, upper)

guess = int(input("Great, now guess a number between " + str(lower) + " and " + str(upper) + ": "))

while guess != number:
    if guess < number:
        print("Nope, too low.")
    else:
        print("Nope, too high.")

    guess = int(input("Guess another number: "))

print("You got it!")
