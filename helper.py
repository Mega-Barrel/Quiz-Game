import random

from questions.ToF_questions import ToF as s1
from questions.sports_questions import sport_ques as s2
from questions.Geography_question import geography_question as s3

def play_quiz(pass_input):
    if pass_input == '1':
        s = s1()
    elif pass_input == '2':
        s = s2()
    elif pass_input == '3':
        s = s3()
        
    random.shuffle(s)
    score = 0

    for i in s:
        
        print(i[0])
        guess = input('Enter answer: ')
        
        if guess == i[1].lower() or guess == i[1]:
            score = score + 1
        
        print()
    
    print('Final score is: '+str(score))
