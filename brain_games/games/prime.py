from random import randint
from brain_games.games import constants


def instructions():
    print(constants.PRIME_INSTRUCTION)


def is_prime(x):
    count = 0
    for i in range(2, x // 2 + 1):
        if (x % i == 0):
            count = count + 1
    if (x == 1):
        return False
    elif (count == 0):
        return True
    else:
        return False


def question():
    num = randint(2, 100)
    if is_prime(num):
        res = 'yes'
    else:
        res = 'no'
    eng_task = str(num)
    return eng_task, res
