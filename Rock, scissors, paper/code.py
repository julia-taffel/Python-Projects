import random
answers = ('rock', 'paper', 'scissors')
print('Welcome to the rock, paper & scissors game with computer!')
willing = 'yes'
gamer_1 = input('Enter your name: ')
while willing == 'yes':
    answer_1 = input(' %s: Choose rock, scissors or paper: ' % gamer_1)  
    comp_answer = random.choice(answers)
    print('Computer chose: ' + comp_answer)

    def compare(answer_1, comp_answer):
        if answer_1 == comp_answer:
            return('That is a draw')
        elif answer_1 == 'rock':
            if comp_answer == 'paper':
                return('Paper wins')
            elif comp_answer == 'scissors':
                return('Rock wins')
        elif answer_1 == 'scissors':
            if comp_answer == 'paper':
                return('Scissors win')
            elif comp_answer == 'rock':
                return('Rock wins')
        elif answer_1 == 'paper':
            if comp_answer == 'rock':
                return('Paper wins')
            elif comp_answer == 'scissors':
                return('Scissors win')
        else:
            return('Invalid Entry')
          
    print(compare(answer_1, comp_answer))
    willing = input('Do you want to play one more time? ')
    if willing == 'yes':
        continue
    else:
        break
