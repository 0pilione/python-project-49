#!/usr/bin/env python3


def instructions_gsd():
    print('Find the greatest common divisor of given numbers.')


def question_gsd():
    a = randint(1, 10)
    b = randint(1, 10)
    res = str(math.gcd(a, b))
    eng_task = str(a) + ' ' + str(b)
    return eng_task, res
