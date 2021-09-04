import pandas as pd
import folium
from folium import plugins

data = pd.read_csv('D:/Database/Python/資料檔案/台北市.csv', encoding='ansi',  delimiter=',', dtype={
        'X': 'float16',
        'Y': 'float16'
    })
park_map = folium.Map(location=[data['Y'].mean(), data['X'].mean()], zoom_start=10, control_scale=True, tiles= 'stamen watercolor')
marker_cluster = plugins.MarkerCluster().add_to(park_map)

for name,row in data.iterrows():
    folium.Marker(location=[row["Y"], row["X"]], tooltip=[row['Z']]).add_to(marker_cluster)
park_map.save('park_map2.html')