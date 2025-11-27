from flask import Blueprint, request, jsonify
from services_content import get_all_content, get_content_details

content_bp = Blueprint("content", __name__)

@content_bp.get("/content")
def list_content():
    filters = request.args.to_dict()
    return jsonify(get_all_content(filters))

@content_bp.get("/content/<content_id>")
def content_info(content_id):
    return jsonify(get_content_details(content_id))
