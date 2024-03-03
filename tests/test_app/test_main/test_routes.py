"""
Unit tests for the Flask application routes in the Multi-Vendor Marketplace.

This module contains two test classes:
- TestRoutesDocs: For testing PEP 8 compliance of the routes module.
- TestRoutes: For testing the functionality of application routes.
"""

import unittest
import pep8

from app import create_app, main
from config import TestingConfig


class TestRoutesDocs(unittest.TestCase):
    """
    Test class for checking PEP 8 compliance in the routes module.
    """

    def test_pep8_conformance(self):
        """
        Test that the routes module conforms to PEP 8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['app/main/routes.py'])
        self.assertEqual(result.total_errors, 0, result.messages)


class TestRoutes(unittest.TestCase):
    """
    Test class for testing routes in the Flask application.
    """

    def setUp(self):
        """
        Set up the test client and push the application context.
        """
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """
        Pop the application context.
        """
        self.app_context.pop()

    def test_home_route(self):
        """
        Test the home route to ensure it returns a 200 status code.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
