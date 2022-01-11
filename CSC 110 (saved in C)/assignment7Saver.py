convert_num = 0
valid_date = True

date_string = date_string.split('-')
update = ['year','month','day']

update[0] = 2000 + int(date_string[2])
update[1] = date_string[1]
if update[1] == 'Jan':
    convert_num = 1
elif update[1] == 'Feb':
    convert_num = 2
elif update[1] == 'Mar':
    convert_num = 3
elif update[1] == 'Apr':
    convert_num = 4
elif update[1] == 'May':
    convert_num = 5
elif update[1] == 'Jun':
    convert_num = 6
elif update[1] == 'Jul':
    convert_num = 7
elif update[1] == 'Aug':
    convert_num = 8
elif update[1] == 'Sep':
    convert_num = 9
elif update[1] == 'Oct':
    convert_num = 10
elif update[1] == 'Nov':
    convert_num = 11
elif update[1] == 'Dec':
    convert_num = 12
update[1] = convert_num
update[2] = int(date_string[0])
if update[1] == 1:
    if update[2] not in range(1,32):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 2:
    if update[2] not in range(1,29):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 3:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 4:
    if update[2] not in range(1,30):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 5:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 6:
    if update[2] not in range(1,30):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 7:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 8:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 9:
    if update[2] not in range(1,30):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 10:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 11:
    if update[2] not in range(1,30):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
elif update[1] == 12:
    if update[2] not in range(1,31):
        valid_date = False
        if valid_date == False:
            return 'invalid date'
update = tuple(update)
return update

def date(year:int,month:int,day:int) -> tuple:
    '''
    Enter year, month and day to create a tuple for it
    
    Preconditions: all numbers must be positive integer
    
    >>> date(1966,9,26)
    (1966, 9, 26)
    >>> date(1968,8,5)
    (1968, 8, 5)
    '''
    date_tuple = ('origin','final',0)
    update = list(date_tuple)
    update[0] = year
    update[1] = month
    update[2] = day
    date_tuple = tuple(update)
    return date_tuple

def Netflix_info(show_type:str,title:str,director_names:list[str],actor_names:[str],show_added_date:[int]) -> tuple:
    '''
    Enter type of show,title of show,list of show director names,list of show actor names and date the show added to create a tuple for it
    
    >>> Netflix_info('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Louis C.K.', 'Jeffrey Tambor', 'Fionnula Flanagan', 'Rob Lowe', 'Tina Fey', 'Donna Sorbello', 'Stephanie March'], (2020, 1, 1))
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Louis C.K.', 'Jeffrey Tambor', 'Fionnula Flanagan', 'Rob Lowe', 'Tina Fey', 'Donna Sorbello', 'Stephanie March'], (2020, 1, 1))
    '''
    Info_tuple = ('','',[],[],0)
    update = list(Info_tuple)
    update[0] = show_type
    update[1] = title
    update[2] = director_names
    update[3] = actor_names
    update[4] = show_added_date
    Info_tuple = tuple(update)
    return Info_tuple