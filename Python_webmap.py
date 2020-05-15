import folium
import pandas
# Accessing the Mountains database and extracting Properties.
data =  pandas.read_csv("mountains.csv")

lat = data["Latitude"]
lon = data["Longitude"]
ele = data["Height in ft"]
name = data["Mountain"]

#Accessing India Top 50 Tourism Places database and extracting Properties.
tourismdata = pandas.read_csv("indiatop50.csv")

lat_tourism = tourismdata["Latitude"]
lon_tourism = tourismdata["Longitude"]
place_tourism = tourismdata["Place"]
state_tourism = tourismdata["State"]
name_tourism = tourismdata["Name"]
symbol_tourism = tourismdata["Placesymbol"]

#Function used to color mountain markers according to their Height.
def color_producer(elevation):
    if elevation < 23000:
        return 'green'
    elif 23000 <= elevation < 25000:
        return 'orange'
    else:
        return 'red'

#Function used to give tourism places their marker icon according to their type.
def iconset(symbol):
    if symbol == 'F':               #For fort
        return 'tower' 
    elif symbol == 'P':             #For Palace
        return 'queen' 
    elif symbol == 'N':             #For Nature
        return 'tree-conifer'
    elif symbol == 'H':             #For Historical places
        return 'map-marker'
    elif symbol == 'R':             #FOr Religious Places
        return 'heart'    

toollip = 'Click here'

#Set initial focus of map and zoom levels.
map = folium.Map(location=[23.239733, 77.419613 ], zoom_start=4.6, tiles='Stamen Terrain' )

#To inittialize feature Group.
fgm = folium.FeatureGroup(name = "Mountains")

for lt, ln, el, nm in zip(lat, lon, ele, name):
    fgm.add_child(folium.Marker(location = [lt,ln], popup=nm ,tooltip=toollip, icon=folium.Icon(color=color_producer(el),icon='play',angle=270 )))

#Another feature group.
fgp = folium.FeatureGroup(name = "Tourism places")

for lati,longi,name,state,place,symb in zip(lat_tourism,lon_tourism,name_tourism,state_tourism,place_tourism,symbol_tourism):
    fgp.add_child(folium.Marker(location = [lati,longi],popup=name+ "\n" + place + ',' + state ,tooltip=toollip, icon = folium.Icon(icon=iconset(symb))))


#Adding feature groups as child of map features.
map.add_child(fgp)
map.add_child(fgm)
map.add_child(folium.LayerControl())

#saving map as Webpage 
map.save("IndiaTourism.html")