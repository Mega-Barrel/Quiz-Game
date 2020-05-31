import random

from questions.sports_questions import statements as s2
from questions.ToF_questions import statements as s1

def play_quiz(pass_input):
    if pass_input == '1':
        s = s1()
    elif pass_input == '2':
        s = s2()
        
    random.shuffle(s)
    score = 0

    for i in s:
        
        print(i[0])
        guess = input('Enter answer: ')
        
        if guess == i[1].lower() or guess == i[1]:
            score = score + 1
        
        print()
    
    print('Final score is: '+str(score))
