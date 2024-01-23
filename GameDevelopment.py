import random

def play_game():
    value = [1, 2, 3]
    print('1. Rock\n2. Paper\n3. Scissors')

    user = int(input('Enter your action no:'))

    if user < 1 or user > 3:
        print('Invalid input')
    else:
        comp = random.randint(1, len(value))
        print('Computer action is:', comp)
        if comp == user:
            print('Match Draw')
        elif (comp == 1 and user == 3) or (comp == 2 and user == 1) or (comp == 3 and user == 2):
            print('Computer wins!')
        else:
            print('You win!')

while True:
    play_game()
    play_again = input('Do you want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break
