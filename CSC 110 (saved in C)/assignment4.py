import math
import doctest

def is_proper_divisor(num1:int,num2:int) -> bool:
    '''
    The function will determine whether n1 is a proper divisor of n2.
    
    Preconditions: num1 and num2 >= 0
    >>> is_proper_divisor(3,5)
    False
    >>> is_proper_divisor(0,20)
    False
    >>> is_proper_divisor(5,0)
    True
    '''
    if num1 == 0:
        return False
    elif num2 == 0:
        return True
    else:
        if num2 % num1 == 0:
            return True
        else:
            return False
    
def sum_of_proper_divisors(Num:int) -> None:
    '''
    The function will return the sum of the all the proper divisors of that number excluding itself.
    
    Preconditions: sum >= 0
    >>> sum_of_proper_divisors(12)
    16
    '''
    result = 0
    if(Num == 0):
        return 0
    elif(Num == 1):
        return 1
    for num in range(2,(int)(math.sqrt(Num))+1) :
        if (Num % num == 0) :
            if (num == (Num/num)) :
                result += num
            else :
                result += (num + Num//num)
    return (result + 1)

def get_abundance(num:int) -> int:
    '''
    Enter a number and this function will return the abundance of the number entered.
    
    Preconditions: num >= 0
    >>> get_abundance(12)
    4
    >>> get_abundance(0)
    0
    '''
    result = 0
    if(num < 12):
        return 0
    for num1 in range(2,(int)(math.sqrt(num))+1) :
        if (num % num1 == 0) :
            if (num1 == (num/num1)) :
                result += num1
            else :
                result +=(num1 + num//num1)
    if (result + 1 <= num):
        return 0
    else:
        return (result + 1 - num)    
    
def get_multiples(num1:int,num2:int,num3:int) -> str:
    '''
    Enter three numbers and this function will returns a string containing a sequence of multiples separated by at least one space. 
    >>> get_multiples(8,2,7)
    '8 10 12 14 16 18 20'
    >>> get_multiples(9,3,6)
    '9 12 15 18 21 24'
    '''
    answer = ''
    for value in range(num1,num1 + num2 * num3,num2):
        if value != num1 + num2 * (num3-1):
            answer += (str(value)+' ')
        else:
            answer += (str(value))
    return answer
    
def print_multiplication_table(HA:int,VA:int,width:int,height:int):
    '''
    Enter four numbers and this prints a multiplication table to the screen.
    
    >>> print_multiplication_table(0,3,4,10)
    '''
    for num1 in range(height):
        for num2 in range(width):
            if num1%2 == 0:
                print(HA,VA,sep=' ',end=' ')
            else:
                print(VA,HA,sep=' ',end=' ')
        print()