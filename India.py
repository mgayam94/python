import folium
import pandas

data = pandas.read_csv("india.txt")
lat=list(data["LAT"])
lon=list(data["LONG"])
state=list(data["STATES"])

html = """<h4>State Information:</h4> 
Name: %s
"""

map=folium.Map(location=[20.5937, 78.9629], zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
for lt,ln,st in zip(lat,lon,state):
	iframe =  folium.IFrame(html=html % str(st), width=200, height=100)
	fg.add_child(folium.Marker(location=[lt,ln],popup=str(st), icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("india.html") #an HTML file will be created in the current directory as india.html