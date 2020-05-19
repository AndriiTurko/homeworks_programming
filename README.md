# Internet Users Counter

Description:

Nowadays most people in civilized world use Internet, but do you what is the exact amount of them in each country
or how many there were users ten or twenty years ago. This project is aimed to help people in this question.
It analyzes files with population and percentage of Internet users in each country and show a dependency chart
for them on map.
To use the site(http://andr1211.pythonanywhere.com/) you input: years - First year and Last year in interval between 1980 and 2017; country - all,
if you want to see all counries, name of the country in English to see one country and one of the abbreviations of
continents(Europe - EU, South America - SA, North America - NA, Asia - AS, Africa - AF, Oceania - OC).

Modules:
* country_queue.py - represents Country_Queye ADT
* flask_users.py - creates flask app
* graph.py - builds a dependancy chart of years and users
* json_make_dict.py - makes a dictionary with continents as keys and listc with countries as values
* main.py - checks the input information
* make_locations_json.py makes a json file with countries and their locations
* myarray.py - represents Array class
* reader.py	- parses files with information and counts users in the country of one certain year
* users_map.py - bulids map

Credits:
Turko Andrii, UCU, 2020

License:
[MIT License](https://github.com/AndriiTurko/homeworks_programming/blob/master/LICENSE)
