"""
Contains the forms used for user authentication in the Flask application.

This module defines the structure and validation for user registration and
login forms using WTForms.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    This form collects the first name, last name, email, and password for user
    registration.
    It includes data validation checks for each field to ensure all necessary
    information is provided and conforms to the expected format.
    """
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(min=3, max=50)]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(min=3, max=50)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), Length(max=50)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=50)]
    )
    password2 = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """
    Form for user login.

    This form allows users to log in using their email and password.
    It includes a "Remember Me" option for users who wish to remain logged in
    across sessions.
    """
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), Length(max=50)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=50)]
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
