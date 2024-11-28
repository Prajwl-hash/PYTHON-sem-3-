import random


def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print("Congratulations! You guessed it!")


guess_the_number()
