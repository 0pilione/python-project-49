#!/usr/bin/env python3

from random import randint


def instructions():
    print('What is the result of the expression?')


def question():
    a = randint(1, 10)
    b = randint(1, 10)
    op = randint(1, 3)
    res = 0
    op_str = ''
    if op == 1:
        op_str = ' - '
        res = str(a - b)
    elif op == 2:
        op_str = ' + '
        res = str(a + b)
    elif op == 3:
        op_str = ' * '
        res = str(a * b)

    eng_task = str(a) + op_str + str(b)
    return eng_task, res
