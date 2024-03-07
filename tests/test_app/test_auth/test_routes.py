"""
Unit tests for the authentication routes in the Multi-Vendor Marketplace.

This module contains two test classes:
- TestRoutesDocs: For testing PEP 8 compliance of the auth routes module.
- TestRoutes: For testing the functionality of the authentication routes.
"""

import unittest
import pycodestyle
import flask

from app import create_app
from config import TestingConfig


class TestRoutesDocs(unittest.TestCase):
    """
    Test class for checking PEP 8 compliance in the auth routes module.
    """

    def test_pep8_conformance(self):
        """
        Test that the auth routes module conforms to PEP 8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['app/auth/routes.py'])
        self.assertEqual(result.total_errors, 0, result.messages)


class TestRoutes(unittest.TestCase):
    """
    Test class for testing the authentication routes in the Flask application.
    """

    def setUp(self):
        """
        Set up the test client and create the application context.
        """
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """
        Pop the application context and remove the database session.
        """
        flask.g.pop('session', None)
        self.app_context.pop()

    def test_register_route(self):
        """
        Test the /auth/register route to ensure it is accessible.
        """
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200,
                         "Register route inaccessible.")

    def test_login_route(self):
        """
        Test the /auth/login route to ensure it is accessible.
        """
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200,
                         "Login route inaccessible.")

    def test_logout_route(self):
        """
        Test the /auth/logout route behavior for an unauthenticated user.
        Adjust the expected status code based on the actual application
        behavior.
        """
        response = self.client.get('/auth/logout')
        self.assertEqual(response.status_code, 401,
                         "Unexpected status code for logout route when "
                         "unauthenticated.")


if __name__ == '__main__':
    unittest.main()
