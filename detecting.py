from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
def detecting_anomalies(clean_flights):
    if not clean_flights or len(clean_flights) < 2:
        return []
    features=[]
    for plane in clean_flights:
        velocity=plane[9]
        altitude=plane[7]
        vertical_rate=plane[11]
        features.append([velocity,altitude,vertical_rate])
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    model = IsolationForest(contamination=0.01, random_state=42)
    forest_labels = model.fit_predict(scaled_features)
    detectedanomalies=[]
    lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)
    lof_labels = lof.fit_predict(scaled_features)
    for i in range(len(clean_flights)):
        if forest_labels[i]==-1 and lof_labels[i]==-1:
            detectedanomalies.append(clean_flights[i])
    return detectedanomalies