import uuid
from database import db


# ---------- SUBSCRIPTION PLANS ----------

def create_subscription(data):
    plan = {
        "_id": str(uuid.uuid4()),
        "plan_name": data["plan_name"],
        "monthly_price": data["monthly_price"],
        "max_profiles": data["max_profiles"]
    }
    db.subscription_plans.insert_one(plan)
    return {"subscription_id": plan["_id"]}

def get_subscriptions():
    plans = list(db.subscription_plans.find())
    for p in plans:
        p["subscription_id"] = p.pop("_id")
    return plans

def update_subscription(plan_id, data):
    db.subscription_plans.update_one(
        {"_id": plan_id},
        {"$set": data}
    )
    return {"message": "Subscription plan updated"}

def delete_subscription(plan_id):
    db.subscription_plans.delete_one({"_id": plan_id})
    return {"message": "Subscription plan deleted"}


# ---------- USER MANAGEMENT ----------

def get_users():
    users = list(db.users.find({}, {"password": 0}))
    for u in users:
        u["user_id"] = u.pop("_id")
    return users

def delete_user(user_id):
    db.users.delete_one({"_id": user_id})
    return {"message": "User deleted"}


# ---------- CONTENT MANAGEMENT ----------

def create_content(data):
    content = {
        "_id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "content_type": data["type"]
    }
    db.content.insert_one(content)

    # Genre links
    for genre_id in data.get("genres", []):
        db.content_genre.insert_one({
            "_id": str(uuid.uuid4()),
            "content_id": content["_id"],
            "genre_id": genre_id
        })

    # Seasons & Episodes for TV only ig?
    for season in data.get("seasons", []):
        season_id = str(uuid.uuid4())
        db.seasons.insert_one({
            "_id": season_id,
            "series_id": content["_id"],
            "season_number": season["season_number"],
            "release": season.get("release_date")
        })

        for ep in season.get("episodes", []):
            db.episodes.insert_one({
                "_id": str(uuid.uuid4()),
                "season_id": season_id,
                "episode_number": ep["episode_number"],
                "title": ep["title"],
                "duration": ep["duration"]
            })

    return {"content_id": content["_id"]}


def update_content(content_id, data):
    db.content.update_one({"_id": content_id}, {"$set": data})
    return {"message": "Content updated"}


def delete_content(content_id):
    db.content.delete_one({"_id": content_id})
    db.content_genre.delete_many({"content_id": content_id})
    db.media_files.delete_many({"content_id": content_id})
    return {"message": "Content deleted"}


# ---------- GENRES ----------

def create_genre(data):
    genre = {
        "_id": str(uuid.uuid4()),
        "genre_name": data["genre_name"]
    }
    db.genres.insert_one(genre)
    return {"genre_id": genre["_id"]}

def get_genres():
    genres = list(db.genres.find())
    for g in genres:
        g["genre_id"] = g.pop("_id")
    return genres

def delete_genre(genre_id):
    db.genres.delete_one({"_id": genre_id})
    return {"message": "Genre deleted"}


# ---------- MEDIA FILES ----------

def add_media_file(content_id, data):
    media = {
        "_id": str(uuid.uuid4()),
        "content_id": content_id,
        "file_path": data["file_path"],
        "resolution": data["resolution"],
        "language": data["language"],
        "file_size": data["file_size"]
    }
    db.media_files.insert_one(media)
    return {"media_file_id": media["_id"]}

def delete_media_file(media_id):
    db.media_files.delete_one({"_id": media_id})
    return {"message": "Media file deleted"}
