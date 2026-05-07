from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from db import mongo

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/", methods=["GET"])
@jwt_required()
def get_dashboard():

    total_projects = mongo.db.projects.count_documents({})

    total_tasks = mongo.db.tasks.count_documents({})

    completed_tasks = mongo.db.tasks.count_documents({
        "status": "completed"
    })

    pending_tasks = mongo.db.tasks.count_documents({
        "status": "pending"
    })

    inprogress_tasks = mongo.db.tasks.count_documents({
        "status": "in-progress"
    })

    return jsonify({
        "total_projects": total_projects,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "inprogress_tasks": inprogress_tasks
    })