from random import randint


def main():
    pass
    # ab = 'x'


def salut():
    salut_name = input('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {salut_name}!')
    return salut_name


def question(quest_task):
    print(f'Question: {quest_task}')
    quest_d = input('Your answer: ')
    return quest_d


def engine():
    a = randint(1, 10)
    b = randint(1, 10)
    op = randint(1, 3)
    res = 0
    op_str = ''
    if op == 1:
        op_str = ' - '
        res = a - b
    elif op == 2:
        op_str = ' + '
        res = a + b
    elif op == 3:
        op_str = ' * '
        res = a * b

    eng_task = str(a) + op_str + str(b)
    return eng_task, res


def check(check_task, check_answ, name):
    if check_task == check_answ:
        print('Correct!')
        return 1
    else:
        print(f"""{check_task} is wrong answer ;(.
Correct answer was {check_answ}.""")
        return 0


name = salut()

print('What is the result of the expression?')

count = 0
ch = 0
while count < 3:
    task, res = engine()
    d = question(task)
    ch = check(int(d), res, name)
    if ch == 1:
        count += 1
        continue
    else:
        break

if ch == 1:
    print(f'Congratulations, {name}!')
else:
    print(f"Let's try again, {name}!")
