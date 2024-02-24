from random import randint
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def question():
    random_number = randint(1, 10)
    random_number_2 = randint(1, 10)
    res = str(math.gcd(random_number, random_number_2))
    eng_task = f'{random_number} {random_number_2}'
    return eng_task, res
