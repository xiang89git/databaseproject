import uuid
from datetime import datetime
from database import db


# PROFILE MANAGEMENT 

def create_profile(data):
    profile = {
        "_id": str(uuid.uuid4()),
        "user_id": data["user_id"],
        "profile_name": data["profile_name"]
    }
    db.profiles.insert_one(profile)
    return profile

def get_profiles(user_id):
    profiles = list(db.profiles.find({"user_id": user_id}, {"_id": 1, "profile_name": 1}))
    for p in profiles:
        p["profile_id"] = p.pop("_id")
    return profiles

def update_profile(profile_id, data):
    db.profiles.update_one({"_id": profile_id}, {"$set": {"profile_name": data["profile_name"]}})
    return {"profile_id": profile_id, "profile_name": data["profile_name"]}

def delete_profile(profile_id):
    db.profiles.delete_one({"_id": profile_id})
    return {"message": "Profile deleted successfully"}


# WISHLIST 

def add_to_wishlist(profile_id, content_id):
    entry = {
        "profile_id": profile_id,
        "content_id": content_id,
        "date_added": datetime.utcnow()
    }
    db.wishlist.insert_one(entry)
    return {"message": "Added to wishlist"}

def get_wishlist(profile_id):
    items = list(db.wishlist.find({"profile_id": profile_id}, {"_id": 0}))
    return items

def remove_from_wishlist(profile_id, content_id):
    db.wishlist.delete_one({"profile_id": profile_id, "content_id": content_id})
    return {"message": "Removed from wishlist"}


# VIEWING HISTORY 

def add_history(profile_id, data):
    entry = {
        "viewing_history_id": str(uuid.uuid4()),
        "profile_id": profile_id,
        "content_id": data["content_id"],
        "last_watched_timestamp": data["timestamp"],
        "last_watched_date": datetime.utcnow(),
        "completed": data.get("completed", False)
    }

    # upsert (updatesif exists)
    db.viewing_history.update_one(
        {"profile_id": profile_id, "content_id": data["content_id"]},
        {"$set": entry},
        upsert=True
    )
    return {"message": "Viewing progress saved"}

def get_history(profile_id):
    history = list(db.viewing_history.find({"profile_id": profile_id}, {"_id": 0}))
    return history
