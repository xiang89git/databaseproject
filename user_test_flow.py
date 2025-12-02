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
    "profile_name": "67kid"
})
profile = resp.json()
print(profile)

profile_id = profile["_id"]
print("User flow is completed")

print("Adding to wishlist...")
resp = requests.post(f"{BASE}/wishlist", json={
    "content_id": token, 
})
wishlist_add = resp.json()
print(wishlist_add)

print("Removing item from the wishlist...")
resp = requests.delete(f"{BASE}/wishlist", token
)
wishlist_delete = resp.json()
print(wishlist_delete)

print("Adding to viewing history...")
resp = requests.post(f"{BASE}/history", json={
    "content_id": token,
})
viewinghistory_add = resp.json()
print(viewinghistory_add)

print("Getting viewing history...")
resp = requests.post(f"{BASE}/history", token
)
viewinghistory_items = resp.json()
print(viewinghistory_items)
