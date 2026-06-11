import json
from cleaning import cleaning_data
from detecting import detecting_anomalies
from mapping import mapping

clean_flights,anomalies_found, totale= cleaning_data()
detected_anomalies= detecting_anomalies(clean_flights)
m=mapping(clean_flights,anomalies_found,detected_anomalies)
#lil Summary
print(f"Started with {totale} planes")
print(f"Clean:            {len(clean_flights)}")
print(f"Rule-based flags: {len(anomalies_found)}")
print(f"ML flags:         {len(detected_anomalies)}")
for i in range(len(detected_anomalies)):
    anomaly = detected_anomalies[i]
    print("plane number",i)
    print("the callsign is: ",anomaly[1])
    print("the altitude is: ",anomaly[7])
    print("the vertical rate is: ",anomaly[11])
    print("the velocity is: ",anomaly[9])
   
with open("anomalies.json", "w") as f:
    json.dump(anomalies_found, f, indent=2)
m.save("flight_map.html")
print("Map saved to flight_map.html")