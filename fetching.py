import requests
import streamlit as st

def fetch_fights():
    response = requests.post(
        "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token",
        data={
            "grant_type": "client_credentials",
            "client_id": st.secrets["CLIENT_ID"],
            "client_secret": st.secrets["CLIENT_SECRET"]
        },
        timeout=10
    )
    token = response.json()["access_token"]
    r = requests.get(
        "https://opensky-network.org/api/states/all",
        headers={"Authorization": "Bearer " + token},
        timeout=10
    )
    data = r.json()
    return data