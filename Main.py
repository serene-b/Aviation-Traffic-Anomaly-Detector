#importing
import requests
import time
import json
import folium
from sklearn.ensemble import IsolationForest
#Data
r=requests.get("https://opensky-network.org/api/states/all")
data = r.json()
cleaned_flights = []
anomalies_found= []
#Cleaning
def Not_empty(icao24,callsign,origin_country,time_position,longitude,latitude,altitude,on_ground,velocity,vertical_rate):
    if callsign is not None and origin_country is not None and time_position is not None and longitude is not None and latitude is not None and icao24 is not None and velocity is not None and altitude is not None and vertical_rate is not None:
        return True
current_time=time.time()
for plane in data['states']:
    icao24 = plane[0]
    callsign = plane[1]
    origin_country=plane[2]
    time_position=plane[3]
    longitude = plane[5]
    latitude = plane[6] 
    altitude = plane[7]
    on_ground=plane[8]
    velocity=plane[9]
    vertical_rate=plane[11]
    if not Not_empty(icao24, callsign, origin_country,time_position, longitude, latitude, altitude, on_ground, velocity, vertical_rate):
        continue  
    if not (-180.0 <= longitude <= 180.0 and -90.0 <= latitude <= 90.0):
        continue
    if velocity > 350:
        continue
    if current_time-time_position>60:
        continue
    if on_ground and velocity > 30:
        anomalies_found.append(plane)  
    elif not on_ground and not (0 <= altitude <= 15000):
        anomalies_found.append(plane)  
    else:
        cleaned_flights.append(plane)

with open("anomalies.json", "w") as f:
    json.dump(anomalies_found, f, indent=2)
#Ml Detections
features=[]
for plane in cleaned_flights:
    velocity=plane[9]
    altitude=plane[7]
    vertical_rate=plane[11]
    features.append([velocity,altitude,vertical_rate])
model = IsolationForest(contamination=0.01, random_state=42)
labels = model.fit_predict(features)
mlanomalies=[]
for i in range(len(labels)):
    if labels[i]==-1:
        mlanomalies.append(cleaned_flights[i])
#lil Summary
print(f"Started with {len(data['states'])} planes")
print(f"Clean:            {len(cleaned_flights)}")
print(f"Rule-based flags: {len(anomalies_found)}")
print(f"ML flags:         {len(mlanomalies)}")
#mapping Data
m = folium.Map(location=[20, 0], zoom_start=3)
for plane in cleaned_flights:
    lat = plane[6]
    lon = plane[5]
    callsign = plane[1] or "Unknown"
    folium.CircleMarker(
        location=[lat, lon],
        radius=3,
        color="green",
        fill=True,
        tooltip=callsign
    ).add_to(m)
for plane in anomalies_found:
    lat = plane[6]
    lon = plane[5]
    callsign = plane[1] or "Unknown"
    folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        color="red",
        fill=True,
        tooltip=callsign
    ).add_to(m)
for plane in mlanomalies:
    lat = plane[6]
    lon = plane[5]
    callsign = plane[1]
    velocity = plane[9]
    altitude = plane[7]
    vertical_rate = plane[11]
    folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        color="orange",
        fill=True,
        tooltip = "ML Anomaly | " + (callsign or "Unknown") + " | Speed: " + str(velocity) + " m/s | Alt: " + str(altitude) + "m | V-rate: " + str(vertical_rate) + " m/s"
    ).add_to(m)
m.save("flights_map_.html")