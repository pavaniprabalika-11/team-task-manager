from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from db import mongo
from middleware.role_middleware import role_required

project_bp = Blueprint("project", __name__)


@project_bp.route("/create", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_project():

    data = request.get_json()

    project = {
        "name": data["name"],
        "description": data["description"],
        "status": "active"
    }

    mongo.db.projects.insert_one(project)

    return jsonify({
        "msg": "Project created successfully"
    }), 201


@project_bp.route("/all", methods=["GET"])
@jwt_required()
def get_projects():

    projects = []

    for project in mongo.db.projects.find():

        project["_id"] = str(project["_id"])

        projects.append(project)

    return jsonify(projects)