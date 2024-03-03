"""
Initializes the main application package.

This module sets up the Flask application, registers blueprints, and loads the
application configuration.
"""

from flask import Flask
from .main import main
from config import Config


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
    app.register_blueprint(main)

    return app
