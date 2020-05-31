
import sys
sys.path.insert(1, 'questions/')

from helper import play_quiz

def main(): 

    print('|------------------------------|')
    print('|------------------------------|')
    print('|------ Welcome To Quiz! ------|')
    print('|                              |')
    print('| 1. True or false quiz        |')
    print('| 2. Sports Trivia Questions   |')
    print('|------------------------------|')
    print('|------------------------------|')

    choice  = input('Enter the quiz option you want to play: ')

    if choice == '1':
        play_quiz(choice)
    elif choice == '2':
        play_quiz(choice)
    else:
        print('Invalid Choice.')

main()




