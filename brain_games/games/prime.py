#!/usr/bin/env python3


def instructions_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_prime():
    num = randint(2, 100)
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        res = 'yes'
    else:
        res = 'no'
    eng_task = str(num)
    return eng_task, res
