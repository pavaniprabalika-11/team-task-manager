from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify

from db import mongo


def role_required(role):

    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            user_id = get_jwt_identity()

            user = mongo.db.users.find_one({
                "_id": user_id
            })

            if not user:
                return jsonify({
                    "msg": "User not found"
                }), 404

            if user["role"] != role:
                return jsonify({
                    "msg": "Access denied"
                }), 403

            return fn(*args, **kwargs)

        return decorator

    return wrapper