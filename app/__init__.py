# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import quote_plus
from config import Config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    "To run the Flask app"
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Load configuration from config.py in the project root directory
    app.config.from_pyfile('config.py', silent=True)

    # Configure Flask to use MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = Config.SECRET_KEY

    # Allow CORS for all domains on all routes
    CORS(app)

    # Initialize the database
    db.init_app(app)

    # Initialize Flask-Bcrypt
    bcrypt.init_app(app)

    # Import blueprints
    from app.controllers.main_controller import main_controller
    from app.controllers.user_controller import user_controller

    # Register blueprints
    app.register_blueprint(main_controller)
    app.register_blueprint(user_controller, url_prefix='/api/v1')

    return app, db, bcrypt


