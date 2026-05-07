from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from db import mongo

load_dotenv()

app = Flask(__name__)

CORS(app)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")

mongo.init_app(app)

jwt = JWTManager(app)

# IMPORT ROUTES
from routes.auth_routes import auth_bp
from routes.project_routes import project_bp
from routes.task_routes import task_bp
from routes.dashboard_routes import dashboard_bp

# REGISTER BLUEPRINTS
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(project_bp, url_prefix="/api/projects")
app.register_blueprint(task_bp, url_prefix="/api/tasks")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")


@app.route("/")
def home():
    return {
        "message": "Backend running successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)