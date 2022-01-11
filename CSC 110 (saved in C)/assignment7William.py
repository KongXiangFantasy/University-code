import doctest

# values comprise a valid date in the calendar
DateInfo = tuple[int, int, int]
DATE_INFO_YEAR = 0
DATE_INFO_MONTH = 1
DATE_INFO_DAY = 2

NetflixShow = tuple[str, str, list[str], list[str], DateInfo]
TYPE_OF_SHOW = 0
TITLE_OF_THE_SHOW = 1
DIRECTOR_NAMES = 2 
ACTOR_NAMES = 3
DATE_INFO = 4

#index information for date month year afrer using split('-') to make the_date
#arugments into a list in the creats dates function
DATE = 0
MONTH = 1
YEAR = 2



def multiply_by(element_list: list, multiplier_list: list[int]) -> list:
    '''
    multiply every element in the element list by the value at the corresponding
    position in the multiplier list
    
    Precondition: only non negative integers for multiplier_list 
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
    element_list_length = len(element_list)
    multiplier_list_length = len(multiplier_list)
    for counts in range(element_list_length):
        if counts <  element_list_length and counts < multiplier_list_length:
            element_list[counts] *= multiplier_list[counts]
    return element_list


def create_date(the_date: str) -> DateInfo:
    '''
    turn 'day-month-year' where day is a 2 digit integer, month is the first 3 
    letters of a valid month, the first letter is uppercase, year is a 2 digit 
    integer representing a year in the 2000s, into a DateInfo tuple type 
    and return
    
    Precondition: the values in the given string comprise a valid date. 
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    '''
    Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    the_date = the_date.split('-')
    year =  int('20' + the_date[YEAR])
    month = Month.index(the_date[MONTH]) + 1
    date = int(the_date[DATE])
    result_tuple = (year, month, date)
    return result_tuple


def create_show(type_of_show: str, title_of_the_show: str, director_name: str,
                actor_names: str, date: str) -> NetflixShow:
    
    '''
    returns a Netflix Show tuple 
    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson', 'Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    >>> create_show('Movie', 'The Bad Kids', 'Keith Fulton:Louis Pepe', '', '01-Apr-17')
    ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1))
    '''
    director_name = director_name.split(':')
    if director_name == ['']:
        director_name = []
    actor_names = actor_names.split(':')
    if actor_names == ['']:
        actor_names = []
    date = create_date(date)
    result_tuple = (type_of_show, title_of_the_show, director_name, actor_names, date)
    return result_tuple
                     
def get_titles(netflix_show: list[NetflixShow]) -> list[str]:
    '''
    return a list of the titles of each of Netflix, in the order of appear
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    '''
    result_list = []
    for netflix_show_tuple in netflix_show:
        if netflix_show_tuple[TITLE_OF_THE_SHOW] not in result_list:
            result_list.append(netflix_show_tuple[TITLE_OF_THE_SHOW])
    return result_list

def is_actor_in_show(netflix_show: NetflixShow, actor_name: str) -> bool:
    '''
    determine whether the actor in the given Netflix show tuple
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)),'Rob Lowe')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)),'roB lowE') 
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Emma Stone')
    False
    '''
    for element_netflix_show in netflix_show:
        for actor_names_element in element_netflix_show[ACTOR_NAMES]:
            if actor_name.upper() in actor_name_uppercase_list:
                return True 
    return False 

def count_shows_before_date(netflix_show: list[NetflixShow], the_date: [DateInfo]) -> int:
    '''
    return the count of the Netflix show tuples for those that added before the given date  
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),  ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),  ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2018, 12, 12))
    2
    '''
    result = 0
    for element_netflix_show in netflix_show:
        if  element_netflix_show[DATE_INFO] < the_date:
            result += 1
    return result 

def get_shows_with_actor(netflix_show_list: list[NetflixShow], actor_name: str) -> list[NetflixShow]:
    '''
    return a list of only the Netflix show tuples that the given actor has acted
    in, in the order of appear 
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),  ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'Emma Stone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    '''
    result_list = []
    for netflix_show_tuple in netflix_show_list:
        for actor_names_element in netflix_show_tuple[ACTOR_NAMES]:
            if actor_names_element.upper() in actor_name.upper():
                if netflix_show_tuple not in result_list:
                    result_list.append(netflix_show_tuple)
    return result_list 