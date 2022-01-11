import doctest
from pet import Pet
from date import Date

# represents a pet as (name, species)
PetNameSpecies = tuple[str,str]

# columns of values within input file row and within PetNameSpecies tuple
NAME    = 0
SPECIES = 1
MONTH   = 2
DAY     = 3
YEAR    = 4

def read_file(file_name: str) -> list[Pet]:
    ''' returns a list of Pets populated with data from filename
    
    Preconditions: filename exists.
    If filename is not empty, each row has a single Pet's information
    separated by commas with expected values at columns:
    NAME, SPECIES, MONTH, DAY and YEAR.

    >>> read_file('empty.csv')
    []
    >>> read_file('pet_data.csv')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    '''
    result_list = []
    
    file_handle = open(file_name, 'r', encoding="utf8")
    
    for line in file_handle:
        line = line.strip()
        if len(line) == 0:
            return result_list
        else:
            line = line.split(',')
            line[MONTH] = int(line[MONTH])
            line[DAY] = int(line[DAY])
            line[YEAR] = int(line[YEAR])
            date = Date(line[MONTH], line[DAY], line[YEAR])
            pet = Pet(line[NAME],line[SPECIES],date)
            result_list.append(pet)
        
    file_handle.close()
    return result_list

def find_pet(lopets: list[Pet], name: str) -> int:
    ''' returns the position of pet with given name in lopets
    Returns -1 if name not found
    Returns the position of the first found if there >1 Pet with the given name
    
    Precondition: name must match case exactly
    ie. 'rover' does not match 'Rover'

    >>> find_pet([], 'Fred')
    -1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Bowser')
    -1
    >>> find_pet([Pet('Red', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    0
    '''
    count = 0
    not_found = -1
    already_have = []
    
    for pet in lopets:
        pet_name = pet.get_name()
        if pet_name == name and len(already_have) == 0:
            already_have.append(pet_name)
            return count
        else:
            count += 1
        
    if already_have == []:
        return not_found
    
def get_all_of_species(lopets: list[Pet], species: str) -> list[Pet]:
    ''' returns a list of all pets of the given species.
    Result list is not necessarily unique, if >1 Pet in lopets has the same name.
    
    Precondition: species must match case exactly
    ie. 'dog' does not match 'Dog'
    
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_all_of_species([], 'Dog')
    []
    >>> get_all_of_species(pets, 'Dog')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_all_of_species(pets, 'Tiger')
    []
    >>> get_all_of_species(pets, 'Hamster')
    [Pet('Chewie', 'Hamster', Date(1, 23, 2009))]
    '''
    result_list = []
    
    for pet in lopets:
        pet_species = pet.get_species()
        if pet_species == species:
            result_list.append(pet)
            
    return result_list


def get_latest_birthdate(lopets: list[Pet]) -> Date:
    ''' returns the latest Date of all birthdates of Pet instances in lopets
    Precondition: lopets is not empty
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_latest_birthdate([Pet('Rover', 'Dog', Date(12, 31, 2010))])
    Date(12, 31, 2010)
    >>> get_latest_birthdate(pets)
    Date(9, 15, 2016)
    '''
    
#    biggest_date = Date(0,0,0)
    
#    for pet in lopets:
#        date = pet.get_birthdate()
#        month = date.get_month()
#        day = date.get_day()
#        year = date.get_year()
        
#        if year > biggest_date.get_year():
#            biggest_date = date
#        elif year == biggest_date.get_year() and (
#            month > biggest_date.get_month()):
#            biggest_date = date
#        elif year == biggest_date.get_year() and (
#            month == biggest_date.get_month()) and (
#                day > biggest_date.get_month()):
#            biggest_date = date
            
#    return biggest_date
    
    biggest_date = Date(0,0,0)
    
    for pet in lopets:
        date = pet.get_birthdate()
        if biggest_date.is_after(date):
            biggest_date = date
            
    return biggest_date

def get_youngest_pets(lopets: list[Pet]) -> list[PetNameSpecies]:
    ''' returns a list of PetNameSpecies of all the youngest pets in lopets
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_youngest_pets([])
    []
    >>> get_youngest_pets(pets)
    [('Red', 'Cat'), ('Scout', 'Dog')]
    '''
    final_list = []
    
    if len(lopets) == 0:
        return final_list
    
    biggest_date = get_latest_birthdate(lopets)
    result_list = []
    
    for pet in lopets:
        date = pet.get_birthdate()
        name = pet.get_name()
        species = pet.get_species()
        
        if date == biggest_date:
            if result_list != []:
                result_list = []
            result_list.append(name)
            result_list.append(species)
            result_tuple = tuple(result_list)
            final_list.append(result_tuple)
            
    return final_list