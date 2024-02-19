from random import randint
import math
from brain_games.games import constants


def instructions():
    print(constants.GSD_INSTRUCTION)


def question():
    random_number = randint(1, 10)
    random_number_2 = randint(1, 10)
    res = str(math.gcd(random_number, random_number_2))
    eng_task = str(random_number) + ' ' + str(random_number_2)
    return eng_task, res
