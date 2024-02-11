#!/usr/bin/env python3


def engine(question, instructions):
    name = input('Welcome to the Brain Games!\n May I have your name?')
    print(f'Hello, {name}!')
    instructions()

    count = 0
    check_res = 0
    while count < 3:
        task, res = question()
        print(f"Question: {task}")
        usr_answ = input('Your answer: ')
        if usr_answ == res:
            print('Correct!')
            check_res = 1
            count += 1
            continue
        else:
            print(f'{usr_answ} is wrong answer ;(.\n Correct answer was {res}.')
            check_res = 0
            break
    if check_res == 1:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
