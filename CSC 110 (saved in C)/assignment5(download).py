import doctest
import random

MIN_DIE = 1
MAX_DIE = 6

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
    die = int(input('enter a simulated dice roll\n'))
    
    return die

