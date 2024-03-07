"""
This module defines the authentication routes for the application.

It includes routes for user registration, login, and logout functionalities.
"""

from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.auth.forms import LoginForm, RegistrationForm
from app.extensions import db
from app.models.user import User
from . import auth


@auth.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """
    Handle requests to the /auth/register route.
    Add a new user to the database through the registration form.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is not None:
            flash(
                'This email address is already associated with an account. '
                'Please log in or use a different email to register.',
                'danger'
            )
        else:
            user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """
    Handle requests to the /auth/login route.
    Log an existing user in.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.home'))

        flash(
            'The email or password you entered is incorrect. '
            'Please try again.',
            'danger'
        )
    return render_template('auth/login.html', title='Login', form=form)


@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    """
    Handle requests to the /auth/logout route.
    Log a user out.
    """
    logout_user()
    return redirect(url_for('main.home'))
