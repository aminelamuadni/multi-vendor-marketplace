"""
Initialization of the 'auth' Blueprint for the Multi-Vendor Marketplace
application.

This module creates a Blueprint named 'auth', used for the auth routes
of the application. The routes for this Blueprint are defined in the
'routes' module.
"""

from flask import Blueprint

# Create a Blueprint named 'auth'
auth = Blueprint('auth', __name__)

# Import the routes module to associate routes with the Blueprint
from . import routes
