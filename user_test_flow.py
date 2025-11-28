# General Service Script

import requests

BASE = "http://localhost:5000/api"

print("Registering User...")
resp = requests.post(f"{BASE}/register", json={
    "first_name": "Bob",
    "last_name": "Smith",
    "email": "bobidk@example.com",
    "password": "skibidibrainrot67",
    "subscription_id": "TEST-SUB"
})
reg = resp.json()
print(reg)

token = reg["token"]
headers = {"user_id": token}

print("Creating profile...")
resp = requests.post(f"{BASE}/profiles", json={
    "user_id": token,
    "profile_name": "If you read this, say 67"
})
profile = resp.json()
print(profile)

profile_id = profile["_id"]
print("User flow is completed")
