def opener(file_name):
    '''Reads file and returns set of lines'''
    st = set()
    with open(file_name, mode='r', encoding='utf-8') as name:
        for temp in name:
            temp = temp.replace('\n', '')
            temp = temp.replace('"', '')
            st.add(temp)
    return st

def make_dict(st):
    '''
    Makes a dictionary from set
    :param st: set made from reading of the file
    :return country_dict: dictionary with country as a key an list of info as value
    '''
    country_dict = {}
    for elem in st:
        if len(elem) > 0:
            temp_lst = elem.split(',')
            country_dict[temp_lst[0]] = (temp_lst[5:-2])
    return country_dict

def info_of_the_year(dicti, country, year):
    '''
    Gets information about certain year of certain country
    :param dicti: dictionary with country as a key an list of info as value
    :param country: country you want get info about
    :param year: year you want info from
    :return info:
    '''
    position = year - 1960
    # print(country, position)
    info = dicti[country][position]
    return info

def count_users(country, year):
    percentage = make_dict(opener('percentage.csv'))
    population = make_dict(opener('population.csv'))
    per = info_of_the_year(percentage, country, year)#percentage of internet users in the country in year
    pop = info_of_the_year(population, country, year)#population of the country in year
    users = float(per) * float(pop) / 100
    return users

# print(count_users('South Korea', 2001))
