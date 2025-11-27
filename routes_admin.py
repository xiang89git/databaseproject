from flask import Blueprint, request, jsonify
from services_admin import (
    create_subscription, get_subscriptions, update_subscription, delete_subscription,
    get_users, delete_user,
    create_content, update_content, delete_content,
    create_genre, get_genres, delete_genre,
    add_media_file, delete_media_file
)

admin_bp = Blueprint("admin", __name__)

# SUBSCRIPTION PLANS
@admin_bp.post("/subscription_plans")
def new_plan():
    return jsonify(create_subscription(request.json))

@admin_bp.get("/subscription_plans")
def all_plans():
    return jsonify(get_subscriptions())

@admin_bp.put("/subscription_plans/<pid>")
def edit_plan(pid):
    return jsonify(update_subscription(pid, request.json))

@admin_bp.delete("/subscription_plans/<pid>")
def remove_plan(pid):
    return jsonify(delete_subscription(pid))

# USERS
@admin_bp.get("/users")
def list_users():
    return jsonify(get_users())

@admin_bp.delete("/users/<uid>")
def remove_user(uid):
    return jsonify(delete_user(uid))

# CONTENT
@admin_bp.post("/content")
def new_content():
    return jsonify(create_content(request.json))

@admin_bp.put("/content/<cid>")
def edit_content(cid):
    return jsonify(update_content(cid, request.json))

@admin_bp.delete("/content/<cid>")
def remove_content(cid):
    return jsonify(delete_content(cid))

# GENRES
@admin_bp.post("/genres")
def new_genre():
    return jsonify(create_genre(request.json))

@admin_bp.get("/genres")
def list_genres():
    return jsonify(get_genres())

@admin_bp.delete("/genres/<gid>")
def remove_genre(gid):
    return jsonify(delete_genre(gid))

# MEDIA FILES
@admin_bp.post("/content/<cid>/media_files")
def new_media(cid):
    return jsonify(add_media_file(cid, request.json))

@admin_bp.delete("/media_files/<mid>")
def remove_media(mid):
    return jsonify(delete_media_file(mid))
