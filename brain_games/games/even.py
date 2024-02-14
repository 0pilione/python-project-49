from random import randint


def instructions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        res = 'yes'
    else:
        res = 'no'
    return random_number, res
