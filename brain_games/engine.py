import prompt


def engine(module):
    name = prompt.string('Welcome to the Brain Games!\n May I have your name?')
    print(f'Hello, {name}!')
    module.instructions()

    count = 0
    check_result = 0
    while count < 3:
        task, res = module.question()
        print(f"Question: {task}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == res:
            print('Correct!')
            check_result = 1
            count += 1
            continue
        else:
            print(f'{user_answer} is wrong answer ;(.\n Correct answer was {res}.') #noqa: E501
            check_result = 0
            break
    if check_result == 1:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
