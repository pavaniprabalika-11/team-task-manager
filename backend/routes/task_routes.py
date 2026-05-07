from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from bson import ObjectId

from db import mongo

task_bp = Blueprint("task", __name__)


@task_bp.route("/create", methods=["POST"])
@jwt_required()
def create_task():

    data = request.get_json()

    task = {
        "title": data["title"],
        "description": data["description"],
        "assigned_to": data["assigned_to"],
        "status": "pending"
    }

    mongo.db.tasks.insert_one(task)

    return jsonify({
        "msg": "Task created successfully"
    }), 201


@task_bp.route("/all", methods=["GET"])
@jwt_required()
def get_tasks():

    tasks = []

    for task in mongo.db.tasks.find():

        task["_id"] = str(task["_id"])

        tasks.append(task)

    return jsonify(tasks)


@task_bp.route("/update/<task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):

    data = request.get_json()

    mongo.db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": {
                "status": data["status"]
            }
        }
    )

    return jsonify({
        "msg": "Task status updated successfully"
    })