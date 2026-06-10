import time
import json
from fetching import fetch_fights

def Not_empty(icao24,callsign,origin_country,time_position,longitude,latitude,altitude,on_ground,velocity,vertical_rate):
    if callsign is not None and origin_country is not None and time_position is not None and longitude is not None and latitude is not None and icao24 is not None and velocity is not None and altitude is not None and vertical_rate is not None:
        return True

def cleaning_data():
    data=fetch_fights()
    current_time=time.time()
    cleaned_flights = []
    anomalies_found= []
    totale=len(data['states'])
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
    return cleaned_flights , anomalies_found, totale
