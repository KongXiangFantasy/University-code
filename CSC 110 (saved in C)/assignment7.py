import doctest

#alias represent a date(year,month,day)
#where all number > 0
date = tuple[int,int,int]
year = 0
month = 1
day = 2

#alias represent a Netflix_info(show type,title,director names,actor names,date added)
#where date should be a valid number
Netflix_info = tuple[str,str,list[str],list[str],int]
show_type = 0
title = 1
director_names = 2
actor_names = 3
date_added = 4

def multiply_by(element_list:list[None],multiplier_list:list[int]):
    '''
    Enter two lists, the number in each position will be multiplied by the
    number in the corresponding position in the other list and a corresponding
    result with all the numbers will be returned
    
    Preconditions:numbers in second list must be non negative integers
    
    >>> multiply_by(['tangent',7.9,-99],[8,6,13])
    ['tangenttangenttangenttangenttangenttangenttangenttangent', 47.400000000000006, -1287]
    >>> multiply_by([3,3,3],[4,5])
    [12, 15, 3]
    >>> multiply_by([1, 2, 3],[2, 4, 0])
    [2, 8, 0]
    >>> multiply_by([1, 2, 3], [2, 4])
    [2, 8, 3]
    >>> multiply_by([1, 2, 3],[2, 4, 0, 2])
    [2, 8, 0]
    >>> multiply_by([],[])
    []
    >>> multiply_by([0],[])
    [0]
    >>> multiply_by([],[0])
    []
    '''
    list1_length = len(element_list)
    list2_length = len(multiplier_list)
    
    for counts in range(list1_length):
        if counts < list1_length and counts < list2_length:
            element_list[counts] *= multiplier_list[counts]
            
    return element_list
    
def create_date(date_string:str) -> date:
    '''
    Enter a string represent a valid date, the function will return a date tuple
    
    Preconditions:First letter of month must be in uppercase, day must be valid date
    
    >>> create_date('10-Feb-15')
    (2015, 2, 10)
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    '''
    convert_num = 0
    
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
    update = tuple(update)
    return update 
    
def create_show(show_type:str,title:str,directors:str,actors:str,date_added:str) -> Netflix_info:
    '''
    Enter show type,title,directors,actors and date the show added, the function will return a Netflix Show tuple for it
    
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    >>> create_show('Movie','The Invention of Lying','Ricky Gervais:Matthew Robinson','Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey','02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))
    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson', 'Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    >>> create_show('Movie', 'The Bad Kids', 'Keith Fulton:Louis Pepe', '', '01-Apr-17')
    ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1))
    '''
    directors_list = directors.split(':')
    if directors_list == ['']:
        directors_list = []
    actors_list = actors.split(':')
    if actors_list == ['']:
        actors_list = []    
    date_added_tuple = create_date(date_added)
    result_list = show_type,title,directors_list,actors_list,date_added_tuple
    result_tuple = tuple(result_list)
    return result_tuple
    
def get_titles(Netflix_Show_tuple:Netflix_info) -> list[str]:
    '''
    Enter a Netflix Show tuple, the function will return a list of Netflix Show tuples in order
    
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    '''
    title_list = []
    for tuples in Netflix_Show_tuple:
        for titles in tuples:
            if tuples[title] not in title_list:
                title_list.append(tuples[title])
        
    return title_list
        
def is_actor_in_show(Netflix_Show_tuple:Netflix_info,actor_name:str) -> bool:
    '''
    Enter a Netflix Show tuple and the name of the actor, the function will determine whether this actor is in this show or not
    
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)),'Rob Lowe')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)),'Rob Lowe')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)),'roB lowE') 
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Emma Stone')
    False
    '''
    actor_in_show = []
    
    for name in Netflix_Show_tuple[actor_names]:
        if name.upper() == actor_name.upper():
            actor_in_show.append(name)
    
    if len(actor_in_show) > 0:
        return True
    else:
        return False

def count_shows_before_date(show_tuples_list:list[Netflix_info],date_tuple:date) -> int:
    '''
    Enter a list of Netflix Show tuple and a date tuple,the function will find out how many shows are before the given date
    
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)),('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],(2018, 12, 12))
    2
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),  ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),  ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2018, 12, 12))
    2
    '''
    before_list = 0
    
    for tuples in show_tuples_list:
        for date in tuples[date_added]:
            if len(str(date)) == len(str(date_tuple[year])):
                if date < date_tuple[year]:
                    before_list += 1
                    break
                elif date > date_tuple[year]:
                    break
            elif len(str(date)) == 2 or len(str(date)) == 1:
                if date < date_tuple[month]:
                    before_list += 1
                    break
                elif date > date_tuple[year]:
                    break                
            elif len(str(date)) == 2 or len(str(date)) == 1:
                if date < date_tuple[day]:
                    before_list += 1
                    break
    
    return before_list

def get_shows_with_actor(Netflix_show_list:list[Netflix_info],actor_name:str) -> list[Netflix_info]:
    '''
    Enter a list of Netflix shows and the name of actor, the function will return a list of the show the actor has acted in
    
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)),('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'Emma Stone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),  ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'Emma Stone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    '''
    result_list = []
    for tuples in Netflix_show_list:
        for name in tuples[actor_names]:
            if name == actor_name:
                result_list.append(tuples)
                break
                
    return result_list