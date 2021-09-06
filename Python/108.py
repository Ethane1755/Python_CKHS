import pandas as pd
import folium
from folium import plugins

data = pd.read_csv('D:/Database/Python_CKHS/Python_CKHS/資料檔案/地圖資料/1081.csv', encoding='ansi',  delimiter=',')
park_map = folium.Map(location=[data['X'].mean(), data['Y'].mean()], zoom_start=10, control_scale=True)
marker_cluster = plugins.MarkerCluster().add_to(park_map)

for name,row in data.iterrows():
    folium.Marker(location=[row["X"], row["Y"]], tooltip=[row['Z']]).add_to(marker_cluster)
park_map.save('108map.html')