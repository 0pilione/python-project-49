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
    first = randint(5, 10)
    step = randint(5, 10)
    length = randint(5, 15)
    ll = randint(1, length - 2)
    stop = first + step * length
    lst_num = list(range(first, stop, step))
    res = lst_num[ll]
    lst_num[ll] = '..'
    eng_task_a = str(lst_num)
    eng_task = eng_task_a.replace(',', '')
    eng_task = eng_task.replace(']', '')
    eng_task = eng_task.replace('[', '')
    eng_task = eng_task.replace("'", "")
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

print('What number is missing in the progression?')

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
