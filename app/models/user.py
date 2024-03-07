"""
Defines the User model for the database and its related operations.

This module contains the definition of the User class, which represents the
user entity in the database. It includes basic user information fields, methods
to set and check passwords, and a property to get the user's full name.
"""

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class User(UserMixin, db.Model):
    """
    A User model that includes fields for storing user information.

    Attributes:
        id (Integer): Unique identifier for the user.
        first_name (String): The first name of the user.
        last_name (String): The last name of the user.
        email (String): The email address of the user.
        password_hash (String): The hashed password for the user.
        created_at (DateTime): The date and time when the user account was
        created.
        updated_at (DateTime): The date and time when the user account was last
        updated.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    def set_password(self, password):
        """
        Sets the user's password by hashing it and storing the hash.

        Args:
            password (str): The plain text password to hash and store.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks a given password against the user's stored password hash.

        Args:
            password (str): The plain text password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self):
        """
        A property to get the full name of the user.

        Returns:
            str: The full name of the user, which is the combination of
                 the first name and last name.
        """
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """
        Representation of the User instance.

        Returns:
            str: A string representation of the user, typically used for
            debugging.
        """
        return f'<User {self.email}>'
