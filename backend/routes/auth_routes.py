from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

from db import mongo

auth_bp = Blueprint("auth", __name__)

bcrypt = Bcrypt()


@auth_bp.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    user = mongo.db.users.find_one({
        "email": data["email"]
    })

    if user:
        return jsonify({
            "msg": "User already exists"
        }), 400

    hashed_pw = bcrypt.generate_password_hash(
        data["password"]
    ).decode("utf-8")

    new_user = {
        "name": data["name"],
        "email": data["email"],
        "password": hashed_pw,
        "role": data["role"]
    }

    mongo.db.users.insert_one(new_user)

    return jsonify({
        "msg": "User created successfully"
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = mongo.db.users.find_one({
        "email": data["email"]
    })

    if user and bcrypt.check_password_hash(
        user["password"],
        data["password"]
    ):

        token = create_access_token(
            identity=str(user["_id"])
        )

        return jsonify({
            "token": token,
            "role": user["role"]
        })

    return jsonify({
        "msg": "Invalid credentials"
    }), 401