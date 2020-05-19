import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
import json
from graph import build_graph
from PIL import Image
import base64


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
    
    user_map = folium.Map(max_zoom=7, min_zoom=2)
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
        dicti_coor[tuple(dicti[q._name])] = (tuple(users), tuple(years), q._name)
        country_names.append(q._name)

    fg_psn = folium.FeatureGroup(name="Users")
    fg_psn.add_child(
        folium.GeoJson(
            data=open('world.json', 'r', encoding='utf-8-sig').read(),
            style_function=lambda x:{
                'fillColor':'red'
                if x['properties']['NAME'] in country_names
                else 'white',
                'color': 'black',
                'weight': 2.5
                }
            )
        ).add_to(user_map)


    for loc in dicti_coor:
        location = loc
        (users, years, country) = dicti_coor[loc]
        build_graph(users, years, country)
        encoded = base64.b64encode(open('graphs/graph'+ country +'.JPG', 'rb').read())
        html = '<img src="data:image/jpeg;base64,{}">'.format
        iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=420, height=308)
        popup = folium.Popup(iframe, max_width=2000)
        folium.Marker(location=[float(location[0]),
                      float(location[1])],
                      popup=popup).add_to(user_map)
        

    user_map.save('templates/users.html')
