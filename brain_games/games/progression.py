from random import randint


INSTRUCTION = 'What number is missing in the progression?'


def question():
    first = randint(5, 10)
    step = randint(5, 10)
    length = randint(5, 15)
    missed = randint(1, length - 2)
    eng_task = ''
    current = first
    result = 0
    for i in range(length):
        if i != missed:
            eng_task += str(current)
            eng_task += ' '
            current += step
        else:
            eng_task += '.. '
            result = current
            current += step
    return eng_task, str(result)
