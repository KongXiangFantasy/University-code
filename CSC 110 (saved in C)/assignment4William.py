import doctest

def is_proper_divisor(n1: int, n2: int) -> bool:
    '''
    determine whether n1 is a proper divisor of n2
    
    Precondition: n1 and n2 are both non-negative integer values
    >>> is_proper_divisor(0,0)
    True
    >>> is_proper_divisor(1,0)
    True
    >>> is_proper_divisor(0,1)
    False
    >>> is_proper_divisor(3,9)
    True
    >>> is_proper_divisor(9,3)
    False
    '''
    
    if n2 == 0:
        return True
    elif n1 == 0:
        return n2 == 0
    else:
        return n2 % n1 == 0

is_proper_divisor(3,9)

def sum_of_proper_divisors(dividend: int) -> int:
    '''
    return the sum of the all the proper divisors of the given integer
    excluding itself
    
    Precondition: the given integer is non-negative 
    >>> sum_of_proper_divisors(12)
    16
    >>> sum_of_proper_divisors(0)
    0
    '''
    the_sum = 0
    for number in range(1, dividend):
        if is_proper_divisor(number, dividend):
            the_sum += number
    return the_sum

def get_abundance(integer: int) -> int:
    '''
    return the abundance of given integer
    return 0 if the given integer is not an abundant number
    
    Precondition: the given integer is non-negative
    >>> get_abundance(12)
    4
    >>> get_abundance(11)
    0
    >>> get_abundance(0)
    0
    '''
    abundance_number = sum_of_proper_divisors(integer) - integer 
    if abundance_number <= 0:
        return 0
    else:
        return abundance_number
def get_multiples(initial_number: int, addend: int, length: int) -> str:
    '''
    returns a string containing a sequence of multiples separated by at 
    least one space
    
    
    Precondtion: all arguments should be none negative integers
    >>> get_multiples(8, 2, 7)
    '8 10 12 14 16 18 20'
    >>> get_multiples(9, 3, 6)
    '9 12 15 18 21 24'
    '''
    result = ''
    if length == 1:
        result += str(initial_number)
    if length >= 1:
        result = str(initial_number) + ' '
        for count in range(1, length):
            the_sum = initial_number + addend
            result += str(the_sum)
            if count < length - 1:
                result += ' '
                initial_number = the_sum
    return result

def print_multiplication_table(horizontal_initial: int, width: int,
                               vertical_initial: int, height: int) -> int:
    '''
    prints a multiplication table
    
    Precondition: horizonal initial is none-negative number, the width is 
    greater than 0, the vertical is non-negative number, the height is greater
    than 0
    >>> print_multiplication_table(0,3,4,10)
    0 1 2
    4 0 4 8
    5 0 5 10
    6 0 6 12
    7 0 7 14
    8 0 8 16
    9 0 9 18
    10 0 10 20
    11 0 11 22
    12 0 12 24
    13 0 13 26
    >>> print_multiplication_table(1,3,4,10)
    1 2 3
    4 4 8 12
    5 5 10 15
    6 6 12 18
    7 7 14 21
    8 8 16 24
    9 9 18 27
    10 10 20 30
    11 11 22 33
    12 12 24 36
    13 13 26 39
    '''
    horizontal_line = ' '
    for row in range(1, height + 2):
        if row == 1:
            for number in range (horizontal_initial, horizontal_initial+width):
                horizontal_line += f'{str(number): >2}'
            print(horizontal_line)
        elif horizontal_initial == 0:
            print (vertical_initial, 0, get_multiples(vertical_initial,
                                                vertical_initial, width - 1))   
            vertical_initial += 1
        else:
            print(vertical_initial, get_multiples(vertical_initial,
                                                  vertical_initial, width))   
            vertical_initial += 1