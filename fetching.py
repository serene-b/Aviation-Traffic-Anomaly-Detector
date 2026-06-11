import requests
import json

def fetch_fights():
    r=requests.get("https://opensky-network.org/api/states/all",timeout=10)
    data = r.json()
    return data