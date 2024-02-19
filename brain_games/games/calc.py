from random import randint
from brain_games.games import constants


def instructions():
    print(constants.CALC_INSTRUCTION)


def calculator(x1, x2, operation):
    res = 0
    if operation == 1:
        res = x1 - x2
    elif operation == 2:
        res = x1 + x2
    elif operation == 3:
        res = x1 * x2
    return res


def question():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    symbol = randint(1, 3)
    symbol_str = ''
    if symbol == 1:
        symbol_str = ' - '
    elif symbol == 2:
        symbol_str = ' + '
    elif symbol == 3:
        symbol_str = ' * '
    eng_task = str(number_1) + symbol_str + str(number_2)
    res = str(calculator(number_1, number_2, symbol))
    return eng_task, res
