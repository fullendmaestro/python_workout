# A function that test user input against a randomly generated value betwee one and 10.


import random


def guessRandomNumber():
    answer = random.randint(0, 10)
    while True:
        guess = int(input('Guess a number between one to ten? '))
        if guess == answer:
            print(f'Correct! The answer is {guess}')
            break
        if guess < answer:
            print(f'Your guess of {guess} is too low!')
        else:
            print(f'Your guess of {guess} is too high!')

guessRandomNumber()