import folium
import pandas

# read data from csv
data = pandas.read_csv('Volcanoes.txt')

lats = list(data['LAT'])
longs = list(data['LON'])
elev = list(data['ELEV'])

def color_maker(elevation):
    '''generate colors based on elevation'''

    if int(elevation) < 1000:
        return 'green'
    elif int(elevation) >= 1000 and int(elevation) < 2000:
        return 'orange'
    else:
        return 'red'

# select map of desired area
map = folium.Map(location=[38.58, -99.09], tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name='myMap')


for lat, lon, el in zip(lats, longs, elev):
    fg.add_child(folium.Marker(location=[lat, lon], popup=str(el) + ' m', radius=6, icon=folium.Icon(color=color_maker(el))))

# adding 'border' like lines across the map - polygon layer
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}

map.add_child(fg)

map.save('map1.html')
