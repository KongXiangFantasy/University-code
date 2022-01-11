import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

def create_date(date_num:str)->list[Date]:
    '''
    change the day month year string to year month day as a date tuple
    >>> create_date('11-Jan-11')
    (2011, 1, 11)
    >>> create_date('21-Mar-19')
    (2019, 3, 21)
    '''

    new_list=list(date_num.split("-"))
   
    month= 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    new_list[1]=month.index(new_list[1])+1
    
    return (int(new_list[2])+2000),(new_list[1]),(int(new_list[0]))



def read_file(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    '''
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!

   
    result_list=[]
    file_handle = open(filename, 'r', encoding="utf8")
    list_of_lines= file_handle.readlines()[1:]
    

    for line in list_of_lines:
       
        line=line.strip()
        list_of_item= line.split(',')    
        type_n = list_of_item[INPUT_TYPE]
        title_n = list_of_item[INPUT_TITLE]
        dir_n = list_of_item[INPUT_DIRECTORS]
        dir_n=(dir_n.split(':'))
        cast_n    = list_of_item[INPUT_CAST]
        cast_n=cast_n.split(':')
        date_n    = list_of_item[INPUT_DATE]
        date_n=  create_date(date_n)
        
        
        new_tuple= type_n,title_n,dir_n,cast_n,date_n
        result_list.append(new_tuple)
             
    file_handle.close()
    return result_list

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    '''
    returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    '''
    # TODO: complete this function according to the documentation
    
    new_list=[]
    
    if not show_data:
        return []
    
    first=show_data[0]
    smallest=first[DATE]
   
    for show_info in show_data:
        show_date=show_info[DATE]
        if show_date[YEAR]< smallest[YEAR]:
            smallest=show_date
       
        if show_date[YEAR]==smallest[YEAR] and show_date[MONTH]<smallest[MONTH]:
            smallest=show_date
          
        if show_date[YEAR]==smallest[YEAR] and show_date[MONTH]== smallest[MONTH] and show_date[DAY]<smallest[DAY]:
            new_list.append(show_info[TITLE])
        if show_date[YEAR]==smallest[YEAR] and show_date[MONTH]== smallest[MONTH] and show_date[DAY]==smallest[DAY]:
            new_list.append(show_info[TITLE])            
    
    return new_list        


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    '''
    returns a list of actor names that are found in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts)
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers', 'Michael Cera', 'Emma Stone', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Om Puri', 'Jonah Hill']
    '''
    # TODO: complete this function according to the documentation
    dict1={}
    result_list=[]
    new_list=[]
           
    if shows ==[]:
        return []
           
    for show_list in shows:
        for name in show_list[3]:
            if name in dict1:
                dict1[name]+=1
            else:
                dict1[name]=1
    for key,value in dict1.items():
        new_list.append((key,value))
             
    new_list.sort(key=lambda x:x[1], reverse=True)
    result_list.append(new_list[0][0])
            
    for index in range(1,len(new_list)):
        if new_list[index][1]==new_list[0][1]:
            result_list.append(new_list[index][0])
                    
    return result_list

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    '''
    returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, [])
    []

    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword)
    [('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]
    '''
    # TODO: complete this function according to the documentation
    new_list=[]
    
    for show_list in show_data:
        title= show_list[TITLE]
        title=title.lower()
     
        for term in terms:
            term=term.lower()
            if term in title:
                new_list.append(show_list)
    return new_list

def query(show_data: list[NetflixShow]) -> list[str]:
    '''
    Returns a list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.
    The returned list is in sorted order and does not contain duplicate entries.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    '''
    # TODO: complete this function according to the documentation
    
    if show_data == []:
            return []
    result_list = []
    most_popular_actors = get_actors_in_most_shows(show_data)
    
    for index in show_data:
        for popular_actor in most_popular_actors:
            if (popular_actor in index[3]) and (index[1] not in result_list):
                result_list.append(index[1])
                
    result_list.sort()
    return result_list       
