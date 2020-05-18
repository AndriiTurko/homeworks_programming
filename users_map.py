import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
import json
from graph import build_graph
from PIL import Image


def get_coordinates(location):
    '''
    (str) -> (tuple)
    Transforms the address into coordinates.
    '''
    try:
        geolocator = Nominatim(user_agent='Me', timeout=10)
        location = geolocator.geocode(location)
        country_location = (location.latitude, location.longitude)
        return country_location
    except:
        return None


def build_map(array):
    '''
    Builds map with countries in colours.
    '''
    print('')
    with open('locations.json', 'r', encoding='utf-8') as f:
        dicti = json.load(f)
    
    user_map = folium.Map(tiles = "OpenStreetMap", max_zoom=7, )
    country_names = []
    dicti_coor = {}
    for q in array:
        years = []
        users = []
        cur = q._qhead
        while cur is not None:
            years.append(cur.year)
            users.append(cur.item)
            cur = cur.next
        build_graph(users, years, q._name)
        graph = Image.open("graph.jpg")
        dicti_coor[tuple(dicti[q._name])] = 'C:\Users\User\Desktop\Домашні завдання ОП\hw\graph.jpg'
        country_names.append(q._name)
    marker_cluster = MarkerCluster().add_to(user_map)

    fg_psn = folium.FeatureGroup(name="Users")
    fg_psn.add_child(
        folium.GeoJson(
            data=open('world.json', 'r', encoding='utf-8-sig').read(),
            style_function=lambda x:{
                'fillColor':'green'
                if x['properties']['NAME'] in country_names
                else 'white',
                'color': 'black',
                'weight': 2.5
                }
            )
        ).add_to(user_map)


    for loc in dicti_coor:
        try:
            location = loc
            folium.CircleMarker(
                location=[float(location[0]),
                float(location[1])],
                popup=dicti_coor[loc],
                fill_color='black', fill_opacity = 0.9,
                radius = 10,
                title=str(len(dicti_coor[loc].split(', ')))).add_to(marker_cluster)
        except:
            continue

    user_map.save('templates/users.html')
