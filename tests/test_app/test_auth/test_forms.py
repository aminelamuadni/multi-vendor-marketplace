"""
Unit tests for the authentication forms in the Multi-Vendor Marketplace.

This module contains two test classes:
- TestFormsDocs: For testing PEP 8 compliance of the auth forms module.
- TestForms: For testing the validation and functionality of the authentication
forms.
"""

import unittest
import flask
import pycodestyle
from flask_wtf.csrf import generate_csrf
from app import create_app
from app.auth.forms import LoginForm, RegistrationForm
from config import TestingConfig


class TestFormsDocs(unittest.TestCase):
    """
    Test class for checking PEP 8 compliance in the auth forms module.
    """

    def test_pep8_conformance(self):
        """
        Test that the auth forms module conforms to PEP 8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['app/auth/forms.py'])
        self.assertEqual(result.total_errors, 0, result.messages)


class TestForms(unittest.TestCase):
    """
    Test class for testing the forms in the auth module.
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

    def test_registration_form_validation(self):
        """
        Test the RegistrationForm to ensure validation works as expected.
        """
        with self.app.test_request_context():
            csrf_token = generate_csrf()
            form = RegistrationForm(
                csrf_token=csrf_token,
                first_name="Test",
                last_name="User",
                email="test@example.com",
                password="securepassword",
                password2="securepassword"
            )
            valid = form.validate()
            if not valid:
                print("Errors:", form.errors)
            self.assertTrue(valid, "RegistrationForm validation failed for "
                            "valid data.")

    def test_login_form_validation(self):
        """
        Test the LoginForm to ensure validation works as expected.
        """
        with self.app.test_request_context():
            csrf_token = generate_csrf()
            form = LoginForm(
                csrf_token=csrf_token,
                email="test@example.com",
                password="securepassword"
            )
            valid = form.validate()
            if not valid:
                print("Errors:", form.errors)
            self.assertTrue(valid,
                            "LoginForm validation failed for valid data.")


if __name__ == '__main__':
    unittest.main()
