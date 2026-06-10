import json
from cleaning import cleaning_data
from detecting import detecting_anomalies
from mapping import mapping

cleaned_data,anomalies_found, totale=cleaning_data()
detected_anomalies= detecting_anomalies()
m=mapping()
#lil Summary
print(f"Started with {totale} planes")
print(f"Clean:            {len(cleaned_data)}")
print(f"Rule-based flags: {len(anomalies_found)}")
print(f"ML flags:         {len(detected_anomalies)}")

with open("anomalies.json", "w") as f:
    json.dump(anomalies_found, f, indent=2)