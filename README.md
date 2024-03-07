# Multi-Vendor Marketplace

## Overview

The Multi-Vendor Marketplace is a web application developed as a portfolio project in the 12-month ALX Software Engineering Programme. This project aims to provide a platform for multiple sellers to create and manage their own online stores, offering a diverse range of products to customers.

## Installation

1. Clone the repository: `git clone <repository_url>`.
2. Change to the directory: `cd multi-vendor-marketplace`.
3. Set up a virtual environment and activate it:
   - Windows: `python -m venv venv` and `venv\Scripts\activate`
   - Unix or MacOS: `python3 -m venv venv` and `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.

## Database Setup

The project utilizes MySQL databases for development and testing. To facilitate easy setup, SQL script files are provided in the project repository.

- `setup_mysql_dev.sql`: This script sets up the MySQL database for the development environment.
- `setup_mysql_test.sql`: This script sets up the MySQL database for the testing environment.

Run these scripts in your MySQL server to create the necessary databases and user privileges. Customize the script if needed to match your local or production environment.

## Database Migrations

- Initial tables are auto-created on the first run of the application.
- For schema changes, use Flask-Migrate:
  - Create a migration: `flask db migrate -m "description of changes"`
  - Apply the migration: `flask db upgrade`
- These steps are necessary for evolving the database schema alongside application development.

## Running the Application

- After completing the installation and database setup, run the application: `flask run`.
- Access the application at `http://localhost:5000`.

## Authentication System

The application uses Flask-WTF for form handling, Flask-Login for session management, and Werkzeug for password hashing to provide a secure and efficient authentication system.

Features:
- User registration with form validation and secure password storage.
- User login with password verification and session management.
- Flask-Login integration for handling user sessions.

## Branching Strategy

### Main Branch
- **`main`**: This is the primary branch where the code always reflects a production-ready state.

### Development Branch
- **`dev`**: This branch is used for ongoing development. New features are merged into this branch before being integrated into the main branch.

### Feature Branches
- For new features or updates, create a branch from `dev`, e.g., `feature/new-feature`.
- Once the feature is complete and tested, it gets merged back into the `dev` branch.

### Workflow
- Regularly update your feature branch with changes from `dev` to minimize conflicts.
- After thorough testing in `dev`, merge changes into `main` for release.
- Use pull requests for merging, facilitating code reviews and discussions.
