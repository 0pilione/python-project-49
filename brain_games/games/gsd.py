#!/usr/bin/env python3

from random import randint
import math


def instructions():
    print('Find the greatest common divisor of given numbers.')


def question():
    a = randint(1, 10)
    b = randint(1, 10)
    res = str(math.gcd(a, b))
    eng_task = str(a) + ' ' + str(b)
    return eng_task, res
