import folium
def mapping(clean_flights,anomalies_found,detected_anomalies):
    m = folium.Map(location=[20, 0], zoom_start=3)
    
    for plane in clean_flights:
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
        
    for plane in detected_anomalies:
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
    return m