from random import randint


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


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
