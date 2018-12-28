import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

def color_based_on_volcano(elevation):
        if elevation<1500:
            return '#A9A9A9'
        elif 1500<=elevation<3000:
            return '#FFFF00'
        else:
            return '#F5DEB3'

map = folium.Map(location = [38.58, -99.9], zoom_start=3, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name = "Volcanoes")
for lat, lon, name, elev in zip(lats, lons, names, elevs):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius = 7, popup=name + ", "+str(elev)+"m high from sea level.",
    fill_color=color_based_on_volcano(elev), color='Gray', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'#FAFAD2' if x['properties']['POP2005'] < 10000000 else '#663399' if 10000000<=x['properties']['POP2005']<20000000
else '#4169E1'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
