import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim



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


def color_change(elev):
    if(elev < 3):
        return('green')
    elif(3 <= elev < 7):
        return('orange')
    else:
        return('red')


def build_map(array):
    '''
    Builds map with countries in different colours
    depending on the amount of internet users.
    '''
    print('')
    

    locations = {}
    for q in array:
        location = q._name
        q.add(get_coordinates(location))
  
    dicti_coor = {}
    for i in locations:
        coor = get_coordinates(i)
        if coor not in dicti_coor and coor != None:
            dicti_coor[coor] = locations[i]
        elif coor != None:
            dicti_coor[coor] = dicti_coor[coor] + ', ' + locations[i]

    user_map = folium.Map(tiles = "CartoDB dark_matter")
    
    marker_cluster = MarkerCluster().add_to(user_map)
    for loc in dicti_coor:
        try:
            location = loc
            folium.CircleMarker(
                location=[float(location[0]),
                float(location[1])],
                color=color_change(len(dicti_coor[loc].split(', '))),
                popup=dicti_coor[loc],
                fill_color='black', fill_opacity = 0.9,
                radius = 10,
                title=str(len(dicti_coor[loc].split(', ')))).add_to(marker_cluster)
        except:
            continue

    user_map.save('templates/friends.html')