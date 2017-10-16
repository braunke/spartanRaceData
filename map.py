import folium
m = folium.Map(
    location=[33.6681, 117.3273],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[33.6681, 117.3273],
    popup='California',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[33.5802, 11.6462],
    popup='Arizona',
    icon=folium.Icon(color='green')
).add_to(m)

folium.Marker(
    location=[30.0974, 96.0783],
    popup='Texas',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[33.67129, -83.94149],
    popup='Georgia',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[47.8289, 122.0149],
    popup='Washington',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)




m.save('index.html')