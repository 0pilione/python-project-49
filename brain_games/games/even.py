from random import randint
from brain_games.games import constants


def instructions():
    print(constants.EVEN_INSTRUCTION)


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def question():
    random_number = randint(1, 100)
    result = ''
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return random_number, result
