import requests

def fetch_fights():
    try:
        response = requests.post(
    "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token",
    data={
        "grant_type": "client_credentials",
        "client_id": "sirinefzbelattou-api-client",
        "client_secret": "CfX6o15biTmRKEuXDDOng4heSBUqYcad"
    }
)
        token = response.json()["access_token"]
        r = requests.get(
    "https://opensky-network.org/api/states/all",
    headers={"Authorization": "Bearer " + token},
    timeout=10
)
        data = r.json()
        return data
    except Exception as e:
        return None