# Aviation-Traffic-Anomaly-Detector
Pulls live flight data from the OpenSky Network API, cleans it, and flags aircraft behaving outside normal physical parameters, either through hard rule violations or statistical outliers detected by an Isolation Forest model. Results are visualized on a world map.
# ColorMeaning
🟢 GreenNormal flight
🔴 RedRule-based anomaly
🟠 OrangeML-detected anomaly
