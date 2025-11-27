import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

def create_user(data):
    user = {
        "_id": str(uuid.uuid4()),
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "password": generate_password_hash(data["password"]),
        "subscription_id": data["subscription_id"],
        "signup_date": datetime.utcnow()
    }

    db.users.insert_one(user)

    return {
        "user_id": user["_id"],
        "email": user["email"],
        "token": user["_id"]
    }

def login_user(data):
    user = db.users.find_one({"email": data["email"]})
    if not user:
        return {"error": "User not found"}

    if check_password_hash(user["password"], data["password"]):
        return {"user_id": user["_id"], "token": user["_id"]}

    return {"error": "Invalid password"}
