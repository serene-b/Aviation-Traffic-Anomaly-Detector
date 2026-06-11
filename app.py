import streamlit as st
from streamlit_autorefresh import st_autorefresh
from cleaning import cleaning_data
from detecting import detecting_anomalies
from mapping import mapping
from streamlit_folium import st_folium

st.set_page_config(page_title="Flight Anomaly Detector", layout="wide")
st_autorefresh(interval=60000, key="refresh")
st.title("✈️ Live Flight Anomaly Detector")
clean_flights , anomalies_found, total_flights=cleaning_data()
detected_anomalies=detecting_anomalies()
map=mapping()
st.sidebar.metric("Total number of flights: ", total_flights)
st.sidebar.metric("total number of clean flights: ", len(clean_flights))
st.sidebar.metric("Number of Detected anomalies (rule based): ", len(anomalies_found))
st.sidebar.metric("Number of Detected anomalies (Ml flags): ", len(detected_anomalies))
st_folium(map, width=1400, height=600)