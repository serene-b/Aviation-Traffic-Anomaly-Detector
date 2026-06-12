import streamlit as st
from streamlit_autorefresh import st_autorefresh
from cleaning import cleaning_data
from detecting import detecting_anomalies
from mapping import mapping
from streamlit_folium import st_folium

st.set_page_config(page_title="Flight Anomaly Detector", layout="wide")
st_autorefresh(interval=600000, key="refresh")
st.title("✈️ Live Flight Anomaly Detector")
try:
    clean_flights, anomalies_found, total_flights = cleaning_data()
    detected_anomalies = detecting_anomalies(clean_flights)
    map = mapping(clean_flights, anomalies_found, detected_anomalies)
    st.sidebar.metric("Total number of flights: ", total_flights)
    st.sidebar.metric("total number of clean flights: ", len(clean_flights))
    st.sidebar.metric("Number of Detected anomalies (rule based): ", len(anomalies_found))
    st.sidebar.metric("Number of Detected anomalies (Ml flags): ", len(detected_anomalies))
    st_folium(map, width=1400, height=600)
except Exception as e:
    st.error(f"Error: {e}")