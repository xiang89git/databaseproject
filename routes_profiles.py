from flask import Blueprint, request, jsonify
from services_profile import (
    create_profile, get_profiles, update_profile, delete_profile,
    add_to_wishlist, get_wishlist, remove_from_wishlist,
    add_history, get_history
)

profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.post("/profiles")
def new_profile():
    return jsonify(create_profile(request.json))

@profiles_bp.get("/profiles")
def list_profiles():
    user_id = request.headers.get("UserID")
    return jsonify(get_profiles(user_id))

@profiles_bp.put("/profiles/<profile_id>")
def edit(profile_id):
    return jsonify(update_profile(profile_id, request.json))

@profiles_bp.delete("/profiles/<profile_id>")
def delete(profile_id):
    return jsonify(delete_profile(profile_id))

# USER'S WISHLIST
@profiles_bp.post("/profiles/<pid>/wishlist")
def add_wish(pid):
    return jsonify(add_to_wishlist(pid, request.json["content_id"]))

@profiles_bp.get("/profiles/<pid>/wishlist")
def get_wish(pid):
    return jsonify(get_wishlist(pid))

@profiles_bp.delete("/profiles/<pid>/wishlist/<cid>")
def remove_wish(pid, cid):
    return jsonify(remove_from_wishlist(pid, cid))

# USER'S VIEWING HISTORY
@profiles_bp.post("/profiles/<pid>/history")
def add_hist(pid):
    return jsonify(add_history(pid, request.json))

@profiles_bp.get("/profiles/<pid>/history")
def get_hist(pid):
    return jsonify(get_history(pid))
