from random import randint


def main():
    ab = 'x'


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


def check(check_task, check_answ, name):
    if check_task == check_answ:
        print('Correct!')
        return 1
    else:
        print(f"""{check_task} is wrong answer ;(.
Correct answer was {check_answ}.""")
        return 0


name = salut()

print('Answer "yes" if given number is prime. Otherwise answer "no".')

count = 0
ch = 0
while count < 3:
    task, res = engine()
    d = question(task)
    ch = check(d, res, name)
    if ch == 1:
        count += 1
        continue
    else:
        break

if ch == 1:
    print(f'Congratulations, {name}!')
else:
    print(f"Let's try again, {name}!")
