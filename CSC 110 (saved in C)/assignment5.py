import doctest
import random

MIN_DIE = 1
MAX_DIE = 6

def get_sum_of_digits(base_num:int) -> int:
    '''
    Enter a number, and this function will returen the sum of each digit in the interger.
    
    >>> get_sum_of_digits(0) 
    0
    >>> get_sum_of_digits(432)
    9
    >>> get_sum_of_digits(-571)
    13
    '''
    result = 0
    if base_num < 0:
        base_num = abs(base_num)
        while base_num > 0:
            digit = base_num % 10
            result += digit
            base_num = base_num // 10
        return result        
    elif base_num == 0:
        return 0
    elif base_num > 0:
        while base_num > 0:
            digit = base_num % 10
            result += digit
            base_num = base_num // 10
        return result
    
def is_harshad_number(origin_num:int) -> bool:
    '''
    Enter a number and this function will determines wether the number you entered was a harshad number or not.
    
    Preconditions: origin_num must be greater than 0
    >>> is_harshad_number(432)
    True
    >>> is_harshad_number(433)
    False
    '''
    if origin_num % get_sum_of_digits(origin_num) == 0:
        return True
    else:
        return False
    
def get_first_n_harshad_numbers(num_of_harshad:int) -> str:
    '''
    The function will return a string contain the first n harshad numbers
    
    Preconditions: num_of_harshad must be greater than 0
    >>> get_first_n_harshad_numbers(0)
    ''
    >>> get_first_n_harshad_numbers(1)
    '1'
    >>> get_first_n_harshad_numbers(20)
    '1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42'
    '''
    list_harshad = []
    initial_num = 1
    
    if num_of_harshad == 0:
        return ''
    else:
        while len(list_harshad) < num_of_harshad:
            if is_harshad_number(initial_num) == True:
                list_harshad.append(initial_num)
                initial_num += 1
            else:
                initial_num += 1
                
        result = ','.join(map(str,list_harshad))
            
    return result

def roll_one_die() -> int:
    """ 
    simulates the roll of a single dice between MIN_DIE and MAX_DIE inclusive 
    and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    #generates a random number between MIN_DIE and MAX_DIE inclusive
    #die = random.randint(MIN_DIE, MAX_DIE)
    
    #for testing to allow you to enter the dice roll you want at the keyboard
    #comment out the line above and uncomment this line:
    die = die = random.randint(MIN_DIE, MAX_DIE)
    
    return die

def play(Guess1:int,Guess2:int,bet_amount:int) -> int:
    '''
    A dice game, enter the two points you want to guess, and finally enter the amount you want to bet. If you lose, you will lose all the bet amount, and if you win, you will get double the amount. If you guess one of them incorrectly, you will get a chance to try again.
    
    Preconditions: All guesses number must be between 1 and 6, the bet must be a whole number that greater than 0
    '''
    chance1_roll_1 = roll_one_die()
    chance1_roll_2 = roll_one_die()
    print('you guessed',Guess1,'and',Guess2,'will be rolled and bet','$',bet_amount,'!')
    
    print('you rolled',chance1_roll_1,chance1_roll_2)
    
    if (Guess1 == chance1_roll_1 and Guess2 == chance1_roll_2) or (Guess1 == chance1_roll_2 and Guess2 == chance1_roll_1):
        print('you guessed both correct!')
        bet_amount *= 3
        print('you now have $',bet_amount)
        return bet_amount
        
    elif (Guess1 == chance1_roll_1 and Guess2 != chance1_roll_2) or (Guess1 != chance1_roll_1 and Guess2 == chance1_roll_2) or (Guess1 != chance1_roll_1 and Guess2 == chance1_roll_1) or (Guess1 == chance1_roll_2 and Guess2 != chance1_roll_1):
        print('you guessed one right!')
        
        if Guess1 == chance1_roll_1:
            print('You get a second chance to roll the dice for your other guess:',chance1_roll_2)
        else:
            print('You get a second chance to roll the dice for your other guess:',chance1_roll_1)
        
        total = chance1_roll_1 + chance1_roll_2
        print('Do not let your roll total',total,'or your second chance is over and you lose')
        
    else:
        print('you guessed both incorrect')
        print('sorry, you lose!')
        bet_amount -= bet_amount
        print('you now have $',bet_amount)
        return bet_amount
        
    while(True):
        chance2_roll_1 = roll_one_die()
        chance2_roll_2 = roll_one_die()
        print('you guessed',Guess1,'and',Guess2,'will be rolled and bet','$',bet_amount,'!')
        
        print('you rolled',chance2_roll_1,chance2_roll_2)
        
        if (Guess1 == chance2_roll_1 and Guess2 == chance2_roll_2) or (Guess1 == chance2_roll_2 and Guess2 == chance2_roll_1):
            print('you guessed both correct!')
            bet_amount *= 3
            print('you now have $',bet_amount)
            return bet_amount        
        
        if total == chance2_roll_1 + chance2_roll_2:
            print('you rolled the losing target1')
            print('your second chance is over...')
            print('sorry you lose!')
            bet_amount -= bet_amount
            print('you now have $0')
            return bet_amount
        
        if chance2_roll_1 == Guess1 or chance2_roll_2 == Guess2:
            print('your second chance is over...')
            if chance2_roll_1 == Guess1:
                print('luckily you got a',Guess1,'during your second chance')
            else:
                print('luckily you got a',Guess2,'during your second chance')
            bet_amount *= 2
            print('you now have','$', bet_amount)
            return bet_amount