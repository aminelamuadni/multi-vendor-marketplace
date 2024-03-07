"""
Unit tests for the User model in the Multi-Vendor Marketplace.

This module contains tests for the User model, ensuring that its attributes
and methods function as expected.
"""

import unittest
from app import create_app
from app.extensions import db
from app.models.user import User
from config import TestingConfig


class TestUserModel(unittest.TestCase):
    """
    Test class for testing the User model in the auth module.
    """

    def setUp(self):
        """
        Set up the test client and create the application context.
        """
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        Pop the application context, drop the database, and remove the session.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """
        Test password hashing and checking for a user.
        """
        user = User(email="test@example.com")
        user.set_password("testpassword")
        self.assertFalse(user.check_password("wrongpassword"))
        self.assertTrue(user.check_password("testpassword"))

    def test_full_name_property(self):
        """
        Test the full name property of a user.
        """
        user = User(first_name="Test", last_name="User")
        self.assertEqual(user.full_name, "Test User")

    def test_user_representation(self):
        """
        Test the string representation of the User model.
        """
        user = User(email="test@example.com")
        self.assertEqual(user.__repr__(), '<User test@example.com>')


if __name__ == '__main__':
    unittest.main()
