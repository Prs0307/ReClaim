from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

# Initialize extensions

def create_app():
    app = Flask(__name__)

    # Load configuration

    # Initialize extensions with app

    # Register Blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    return app
