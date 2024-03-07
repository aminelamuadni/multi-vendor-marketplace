"""
Initializes the main application package.

This module sets up the Flask application, registers blueprints, and loads the
application configuration.
"""

from flask import Flask
from .main import main
from .auth import auth
from .extensions import db, migrate, login_manager, bootstrap
from config import Config
from .models.user import User


def create_app(config_class=Config):
    """
    Create and configure a Flask application instance.

    Args:
        config_class (class): The configuration class to use for the
        application.

    Returns:
        app: The created Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
