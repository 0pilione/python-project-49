#!/usr/bin/env python3


def engine(question, instructions):
    name = input('''Welcome to the Brain Games!
    May I have your name? ''')
    print(f'''Hello, {name}!''')
    instructions()

    count = 0
    ch = 0
    while count < 3:
        task, res = question()
        print(f"Question: {task}")
        user_answer = input('Your answer: ')
        if user_answer == res:
            print('Correct!')
            ch = 1
            count += 1
            continue
        else:
            print(f"""{user_answer} is wrong answer ;(.
Correct answer was {res}.""")
            ch = 0
            break
    if ch == 1:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
