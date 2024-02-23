import random
from random import randint


INSTRUCTION = 'What is the result of the expression?'


def calculate(x1, x2, operation):
    res = 0
    if operation == ' - ':
        res = x1 - x2
    elif operation == ' + ':
        res = x1 + x2
    elif operation == ' * ':
        res = x1 * x2
    return res


def question():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    symbol = random.choice([' - ', ' + ', ' * '])
    eng_task = str(number_1) + symbol + str(number_2)
    res = str(calculate(number_1, number_2, symbol))
    return eng_task, res
