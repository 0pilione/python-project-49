#!/usr/bin/env python3

from random import randint


def instructions():
    print('What number is missing in the progression?')


def question():
    first = randint(5, 10)
    step = randint(5, 10)
    length = randint(5, 15)
    ll = randint(1, length - 2)
    stop = first + step * length
    lst_num = list(range(first, stop, step))
    res = str(lst_num[ll])
    lst_num[ll] = '..'
    eng_task_a = str(lst_num)
    eng_task = eng_task_a.replace(',', '')
    eng_task = eng_task.replace(']', '')
    eng_task = eng_task.replace('[', '')
    eng_task = eng_task.replace("'", "")
    return eng_task, res
