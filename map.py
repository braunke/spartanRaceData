import folium
m = folium.Map(
    location=[39.0997, -94.5786],
    zoom_start=4,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[33.6681, -117.3273],
    popup='California',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[33.5802, -111.6462],
    popup='Arizona',
    icon=folium.Icon(color='green')
).add_to(m)

folium.Marker(
    location=[30.0974, -96.0783],
    popup='Texas',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[33.67129, -83.94149],
    popup='Georgia',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[47.8289, -122.0149],
    popup='Washington',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[48.0487, -114.0778],
    popup='Montana',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[39.8984, -81.8274],
    popup='Ohio',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[41.3317, -74.1213],
    popup='New York',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[39.4817, -106.0384],
    popup='Colorado',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[36.5313, -87.3537],
    popup='Tennessee',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[50.8775, -119.9101],
    popup='British Columbia',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

m.save('index.html')