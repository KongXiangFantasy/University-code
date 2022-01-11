import doctest

def multiply_by(base_list:list[None],multiplier:int) -> list[None]:
    '''
    Enter a list and a number that as a multiplier of this list, this function
    will multiply this list by the multiplier in a new list.
    
    Preconditions: multiplier must be a integer
    
    >>> multiply_by([3,4,5],3)
    [9, 12, 15]
    >>> multiply_by(['hello','my','friend'],3)
    ['hellohellohello', 'mymymy', 'friendfriendfriend']
    >>> multiply_by(['hello','my','friend'],0)
    ['', '', '']
    >>> multiply_by([0,-1,99],5)
    [0, -5, 495]
    '''
    new_list = []
    
    for content in base_list:
        result = content * multiplier
        new_list.append(result)
    return new_list
    
def remove_multiples(multi_list:list[int],base_num:int) -> list[int]:
    '''
    Enter a list and a base number, this function will return the numbers in
    list that is not multiples of the base number
    
    Preconditions: all numbers must be integers, and base number can't be 0
    
    >>> remove_multiples([64,29,73],8)
    [29, 73]
    >>> remove_multiples([64,29,73],-1)
    []
    >>> remove_multiples([64,29,73],-2)
    [29, 73]
    >>> remove_multiples([0,0,0],-2)
    []
    >>> remove_multiples([64,29,0],0)
    [64, 29]
    '''
    result_list = []
    
    if base_num == 0:
        for num in multi_list:
            if num != 0:
                result_list.append(num)
    else:          
        for num in multi_list:
            if num % base_num != 0:
                result_list.append(num)
            
    return result_list

def remove_ends_with(word_list:list[str],end_letter:str) -> list[str]:
    '''
    Enter a list of words and a end letter, the function will return the words
    in list that end letter is not included
    
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'],'at')
    ['ratchet', 'atlas']
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'],'AT')
    ['ratchet', 'atlas']
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'],'')
    []
    '''
    length = len(word_list)
    not_include = []
    end_letter_length = len(end_letter)
    
    if len(end_letter) == 0:
        return not_include
    else:
        for num in word_list:
            num_length = len(num)
            if num_length < end_letter_length:
                not_include.append(num)
            elif num[-end_letter_length:].lower() != end_letter.lower():
                not_include.append(num)
        
    return not_include

def get_index_of_largest(origin_list:list[float]) -> int:
    '''
    Enter a list, and this function will find out the index of largest number in the list
    
    >>> get_index_of_largest([4,5,8])
    2
    >>> get_index_of_largest([4,9.99,9])
    1
    >>> get_index_of_largest([4,-9,0])
    0
    '''
    index = 0
    largest = origin_list[0]
    
    for num in origin_list:
        if num >= largest:
            index_of_largest_num = index
            largest = num
        index += 1
        
    return index_of_largest_num
    
def does_contain_proper_divisor(num_list:list[int],calculation_num:int) -> bool:
    '''
    Enter a list and a calculation number, the function will determine whether
    the given list contains any values that are a 
    proper divisor of the calculation number
    
    Preconditions: all numbers must be integer
    
    >>> does_contain_proper_divisor([80,88,99],2)
    True
    >>> does_contain_proper_divisor([0],2)
    False
    >>> does_contain_proper_divisor([],2)
    False
    >>> does_contain_proper_divisor([],0)
    False
    >>> does_contain_proper_divisor([80,88,99],0)
    True
    >>> does_contain_proper_divisor([0,2,3],7)
    False
    '''
    does_proper_divisor = []
    
    if len(num_list) == 0:
        return False
    elif calculation_num == 0:
        return True
    else:
        for value in num_list:
            if value != 0:
                if value % calculation_num == 0:
                    does_proper_divisor.append('True')
                else:
                    does_proper_divisor.append('False')
            else:
                return False
                
        for word in does_proper_divisor:
            if 'True' in does_proper_divisor:
                return True
            else:
                return False
    
def are_all_less_than_threshold(num_list:list[int],threshold:int) -> bool:
    '''
    Enter a list, and the function will determine is there an integer that is
    less than threshold or not
    
    Preconditions: all numbers must be integer
    
    >>> are_all_less_than_threshold([79,889,9],97)
    True
    >>> are_all_less_than_threshold([779,89,9],97)
    True
    >>> are_all_less_than_threshold([779,89,9],7)
    False
    >>> are_all_less_than_threshold([779,89,9],0)
    False
    '''
    less_than = []
    
    for num in num_list:
        if num < threshold:
            less_than.append('True')
        else:
            less_than.append('False')
            
    for word in less_than:
        if 'True' in less_than:
            return True
        else:
            return False        