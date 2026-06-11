import requests
r = requests.get("https://opensky-network.org/api/states/all", timeout=10)
print(f"Status Code: {r.status_code}")
print(f"Response: {r.text[:200]}") # Print first 200 chars