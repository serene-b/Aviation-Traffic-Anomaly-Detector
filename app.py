import streamlit as st
from streamlit_autorefresh import st_autorefresh
from cleaning import cleaning_data
from detecting import detecting_anomalies
from mapping import mapping
from streamlit_folium import st_folium

st.set_page_config(page_title="Flight Anomaly Detector", layout="wide")
st_autorefresh(interval=600000, key="refresh")
st.title("✈️ Live Flight Anomaly Detector")
st.write("Starting fetch...")
st.write("about to fetch")
result = cleaning_data()
st.write("done fetching", result)