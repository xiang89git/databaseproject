from database import db

def get_all_content(filters):
    query = {}

    if "type" in filters:
        query["content_type"] = filters["type"]

    if "genre" in filters:
        genre = db.genres.find_one({"genre_name": filters["genre"]})
        if genre:
            content_ids = [
                i["content_id"]
                for i in db.content_genre.find({"genre_id": genre["_id"]})
            ]
            query["_id"] = {"$in": content_ids}

    content_list = list(db.content.find(query))
    for c in content_list:
        c["content_id"] = c.pop("_id")
    return content_list


def get_content_details(content_id):
    content = db.content.find_one({"_id": content_id})
    if not content:
        return {"error": "Content not found"}

    content["content_id"] = content.pop("_id")

    # Genres
    genres = db.content_genre.find({"content_id": content_id})
    genre_list = []
    for g in genres:
        genre_doc = db.genres.find_one({"_id": g["genre_id"]})
        if genre_doc:
            genre_list.append(genre_doc["genre_name"])
    content["genres"] = genre_list

    # Media files
    files = list(db.media_files.find({"content_id": content_id}, {"_id": 0}))
    content["media_files"] = files

    # Seasons + Episodes from TV
    if content.get("content_type") == "TV":
        seasons = list(db.seasons.find({"series_id": content_id}))
        for s in seasons:
            s["season_id"] = s.pop("_id")
            episodes = list(db.episodes.find({"season_id": s["season_id"]}))
            for e in episodes:
                e["episode_id"] = e.pop("_id")
            s["episodes"] = episodes
        content["seasons"] = seasons

    return content
