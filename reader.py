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
    info = dicti[country][position]
    return info


if __name__ == "__main__":
    percentage = make_dict(opener('percentage.csv'))
    population = make_dict(opener('population.csv'))
    per = info_of_the_year(percentage, 'Ukraine', 2015)#percentage of internet users in Ukraine in 2015
    pop = info_of_the_year(population, 'Ukraine', 2015)#population of Ukraine in 2015
    users = int(per) * int(pop) / 100
    print(users)