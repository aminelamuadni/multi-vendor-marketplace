"""
Configuration module for the Multi-Vendor Marketplace application.

This module defines the configuration classes for the Flask application,
including the base configuration and a separate configuration for testing.
Environment variables are used to customize database settings.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class with common settings."""

    # Flask secret key, used for session management and security
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                'qyCUNua4jSoTcpucI9fcGMMuPVlaVGfw')

    # Database user environment variable or default
    MYSQL_USER = os.environ.get('MYSQL_USER', 'multi_vendor_marketplace_dev')

    # Database password environment variable or default
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD',
                                    'multi_vendor_marketplace_dev_pwd')

    # Database host environment variable or default
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')

    # Database name environment variable or default
    MYSQL_DB = os.environ.get('MYSQL_DB', 'multi_vendor_marketplace_dev_db')

    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB
    )

    # Track modifications for SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing configuration class, inheriting from the base Config."""

    TESTING = True  # Enable testing mode

    # Flask secret key, used for session management and security
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                'kkAuYHHaYrV2HEyDWquu8hyzDE5tlwc2')

    # Override the database user for testing
    MYSQL_USER = os.environ.get('MYSQL_USER', 'multi_vendor_marketplace_test')

    # Override the database password for testing
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD',
                                    'multi_vendor_marketplace_test_pwd')

    # Database host environment variable or default
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')

    # Override the database name for testing
    MYSQL_DB = os.environ.get('MYSQL_DB', 'multi_vendor_marketplace_test_db')

    # SQLAlchemy database URI for testing
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB
    )
