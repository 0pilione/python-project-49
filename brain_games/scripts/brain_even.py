from random import randint

def start_game() -> Literal[1, 0]:
    random_number: int = randint(a=1, b=100)
    print(f"Question: {random_number}")
    user_answer: str = input('Your answer: ')
    if (user_answer == 'yes' and random_number % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
        print('Correct!')
        return 1
    elif user_answer == 'yes' and random_number % 2 !=0:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!")
        return 0
    elif user_answer == 'no' and random_number % 2 == 0:
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!")
        return 0
    else:
        print(f"it is wrong answer ;(.\n Let's try again, {name}!")
        return 0

def main() -> None:
    name = input('''Welcome to the Brain Games!
May I have your name? ''' )
    print(f"Hello, {name}!\nAnswer 'yes' if the number is even, otherwise answer 'no'.")
    win = 3
    index = 0
    result = 0

    while index < win:
        result: Literal[1, 0] = start_game()
        if result == 0:
            break
        index += 1


    if result == 1:
        print(f'Congratulations, {name}!')