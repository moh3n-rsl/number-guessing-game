import math
import random

lower_bound = 0
upper_bound = 0
numberOfChances = 0
randomInteger = 0

##### initialize method
def init():

    # get lower_bound from user & make sure it is a decimal number
    while True:
        lower_bound = input('Enter lower bound: ')
        if not lower_bound.isdecimal():
            continue
        else: break

    # get upper_bound from user & make sure it is a decimal number
    while True:
        upper_bound = input('Enter upper bound: ')
        if not upper_bound.isdecimal():
            continue
        else: break

    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    randomInteger = random.randint(lower_bound, upper_bound)
    numberOfChances = round(math.log(int(upper_bound) - int(lower_bound) + 1, 2))
    
    print('\n\t You\'v only', numberOfChances, 'chances to guess the integer!\n')
    
    # start the game
    startGame(numberOfChances, randomInteger, lower_bound, upper_bound)
#####

##### start game method
def startGame(numberOfChances, randomInteger, lower_bound, upper_bound):
    
    number_of_guesses = 1
    while number_of_guesses <= numberOfChances:
        
        # get res from user & make sure it is a number & it is between lower_bound & upper_bound
        while True:
            res = input('Guess a number: ')
            if not res.isdecimal() or int(res) < lower_bound or int(res) > upper_bound:
                print('WRONG INPUT') 
                continue
            else: break
        res = int(res)
        

        if res == randomInteger:
            print('Congratulations you did it in', number_of_guesses, 'try')
            break
        else:
            print('You guessed too', 'hight!' if res > randomInteger else 'small!')

        number_of_guesses += 1
    
    print('YOU LOOSE!')
    print("Answer:", randomInteger)
#####

init()