# Multi-Vendor Marketplace

## Overview

The Multi-Vendor Marketplace is a web application developed as a portfolio project in the 12-month ALX Software Engineering Programme. This project aims to provide a platform for multiple sellers to create and manage their own online stores, offering a diverse range of products to customers.

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

## Database Setup

The project utilizes MySQL databases for development and testing. To facilitate easy setup, SQL script files are provided in the project repository.

- `setup_mysql_dev.sql`: This script sets up the MySQL database for the development environment.
- `setup_mysql_test.sql`: This script sets up the MySQL database for the testing environment.

Run these scripts in your MySQL server to create the necessary databases and user privileges. Customize the script if needed to match your local or production environment.
