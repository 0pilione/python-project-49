from random import randint


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_prime(x):
    count = 0
    if (x <= 1):
        return False
    for i in range(2, x // 2 + 1):
        if (x % i == 0):
            count = count + 1
    if (count == 0):
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
