import random

def guessThreeRandNum():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 10)

    answer = { num1 + num2 + num3 }

    uInput1 = input('Guess the first number? ')
    uInput2 = input('Guess the second number? ')
    uInput3 = input('Guess the third number? ')
    
    guess = { uInput1 + uInput2 + uInput3 }

    while True:
        if guess == answer:
            print(f'Correct! The answer is {guess}')
            break
        if guess < answer:
            print(f'Your guess of {guess} is too low!')
        else:
            print(f'Your guess of {guess} is too high!')
