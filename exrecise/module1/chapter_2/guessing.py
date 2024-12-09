print("NAME : PRAJWAL RAMA NAIK")
print ("NUMBER : 23BTIT137")

import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
