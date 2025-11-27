from flask import Blueprint, request, jsonify
from services_user import create_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    return jsonify(create_user(request.json))

@auth_bp.post("/login")
def login():
    return jsonify(login_user(request.json))

@auth_bp.get("/logout")
def logout():
    return jsonify({"message": "Logged out successfully"})
