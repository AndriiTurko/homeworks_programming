import matplotlib.pyplot as plt
import os

def build_graph(users, years, country):
    '''
    Builds a dependency chart of users and years in country
    '''
    plt.plot(years, users, color='green', marker='o',
             linestyle='dashed', linewidth=2, markersize=10)
    plt.xlabel('years')
    plt.ylabel('users')

    plt.title('Internet users in ' + country)
    # plt.figure(figsize=(2,1))
    plt.savefig('graph.jpg')


# print(build_graph([23566, 23555, 24000, 23823], [2000, 2001, 2002, 2003], 'Ukraine'))
