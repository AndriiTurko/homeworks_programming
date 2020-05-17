import reader
from json_make_dict import conti_with_count, json_read
from country_queue import CountryQueue
from myarray import Array
from reader import count_users


class Countries:
    '''Represents class, which makes an array 
    of queues with info about countries'''
    def __init__(self, years, countries):
        '''Initializes result, years and countries'''
        self.result = Array(len(countries))
        self.years = years
        self.countries = countries

    def fill_the_array(self):
        '''Fills the array with queues'''
        for index, country in enumerate(self.countries):
            count_q = CountryQueue(country)
            for year in self.years:
                data = count_users(country, year)
                count_q.add(data, year)
            self.result[index] = count_q
        return self.result

    def __str__(self):
        string = ''
        for q in self.result:
            string += q._name + ': ('
            cur = q._qhead
            while cur is not None:
                string += str(cur.year) + ': (' + str(cur.item) + '), '
                cur = cur.next
            string = string[:-2]
            string += ')\n'
        return string

def check_input():
    flag = True
    while flag:
        print('Choose years(between 1960 and 2019) you want get info about.\
            \nInput first and last years of the interval.')
        first_y, last_y = input('First year: '), input('Last year: ')
        if not (first_y.isdigit() and first_y != '' and
                 (last_y.isdigit() or last_y == '')):
            print('Use integer numbers for years!\n')
        else:
            if last_y == '':
                last_y = first_y
            print(last_y)
            first_y = int(first_y)
            last_y = int(last_y)
            if last_y < first_y:
                print('First year should be less than last year!\n')
            elif first_y < 1960 or last_y > 2019:
                print('Please choose years from the given interval.\n')
            else:
                years = [year for year in range(first_y, last_y+1)]
                flag = False

    new_flag = True
    while new_flag:
        continents = conti_with_count()
        print('Choose how many countries you want to see info about.')
        print('All(all), one continent(conti), one country(count).')
        amount = input().lower()
        countries = []
        if amount != 'all' and amount != 'conti' and amount != 'count':
            print('\nInvalid input...\n')
        elif amount == 'all':
            for conti in continents:
                countries += continents[conti]
            new_flag = False
        elif amount == 'conti':
            temp_flag = True
            while temp_flag:
                print('Сhoose continent:\
                    \n(Europe - EU, South America - SA, North America - NA,\
                    Asia - AS, Africa - AF, Oceania - OC, Antarctica - AN)')
                conti = input()
                if conti not in continents:
                    print('\nInvalid input...\n')
                    temp_flag = True
                else:
                    temp_flag = False
            countries += continents[conti]
            new_flag = False
        elif amount == 'count':
            temp_flag = True
            while temp_flag:
                print('Choose country(name in English):')
                country = input()
                if country not in json_read('names.json').values():
                    print('\nInvaid input...\n')
                    temp_flag = True
                else:
                    countries += [country]
                    temp_flag = False
            new_flag = False
    return (years, countries)


def main():
    (years, countries) = check_input()
    result = Countries(years, countries)
    result.fill_the_array()
    # while cur is not None:
    #     print(cur.item)
    #     cur = cur.next
    print(result)
main()
