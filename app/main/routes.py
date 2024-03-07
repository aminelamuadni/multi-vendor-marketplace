"""
Defines routes for the main section of the application.

This module contains the route definitions for the main section, including the
home page and other primary user-facing routes.
"""

from flask import render_template
from . import main


@main.route('/', strict_slashes=False)
def home():
    """
    Render the home page of the Multi-Vendor Marketplace.

    Returns:
        Response: The rendered template for the home page.
    """
    return render_template('home.html',
                           title='Welcome to the Multi-Vendor Marketplace')
