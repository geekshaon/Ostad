# Guess Game v1.1
# Mehedi Hasan

import random

value = random.randint(1, 100)

attempt = 0
print("Welcome to the Number Guessing Game!\nTry to guess the number between 1 and 100.")

while True:
    try:
        userInput = int(input("Enter your guess: "))
        if userInput > value:
            print("Too high!")
            attempt += 1
        elif userInput < value:
            print("Too low!")
            attempt += 1
        elif userInput == value:
            print(f"Congratulations! You've guessed the number in {attempt} attempts.")
            break
    except ValueError:
        print("Please enter a number")
