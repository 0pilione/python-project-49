
def welcome_user():
    nname = ''
    while nname == '':
        print('May I have your name? ', end='')
        nname = input()

        print('Hello, ' + nname + '!')
