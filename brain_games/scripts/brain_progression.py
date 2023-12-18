from random import randint

def main():
    ab = 'x'

def salut():
    salut_name = input('''Welcome to the Brain Games!
May I have your name? ''' )
    print(f'Hello, {salut_name}!')
    return salut_name

def question(quest_task):
    print(f'Question: {quest_task}')
    quest_d = input('Your answer: ')
    return quest_d

def engine():
    first = randint(1, 10)
    step = randint(5, 10)
    length = randint(5, 15)
    l = randint(1, length - 2)
    stop = first + step * length
    lst_num = list(range(first, stop, step))
    res = lst_num[l]
    lst_num[l] = ..
    eng_task = str(lst_num)
    return eng_task, res


def check(check_task, check_answ, name):
    if check_task == check_answ:
        print('Correct!')
        return 1
    else:
        print(f"{check_task} is wrong answer ;(. Correct answer was {check_answ}.")
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
