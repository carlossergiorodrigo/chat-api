"""Main Module"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

DB = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    DB.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        #Routes
        from . import routes

        # Create tables for our models
        DB.create_all()

        return app
