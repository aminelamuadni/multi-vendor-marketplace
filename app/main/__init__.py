"""
Initialization of the 'main' Blueprint for the Multi-Vendor Marketplace
application.

This module creates a Blueprint named 'main', used for the main routes
of the application. The routes for this Blueprint are defined in the
'routes' module.
"""

from flask import Blueprint

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Import the routes module to associate routes with the Blueprint
from . import routes
