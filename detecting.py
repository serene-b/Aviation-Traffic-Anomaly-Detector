from sklearn.ensemble import IsolationForest
from cleaning import cleaning_data

def detecting_anomalies():
    features=[]
    cleaned_flights,_,_=cleaning_data()
    for plane in cleaned_flights:
        velocity=plane[9]
        altitude=plane[7]
        vertical_rate=plane[11]
        features.append([velocity,altitude,vertical_rate])
    model = IsolationForest(contamination=0.01, random_state=42)
    labels = model.fit_predict(features)
    detectedanomalies=[]
    for i in range(len(labels)):
        if labels[i]==-1:
            detectedanomalies.append(cleaned_flights[i])
    return detectedanomalies