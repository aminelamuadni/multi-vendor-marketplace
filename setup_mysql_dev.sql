-- SQL Setup Script for the Multi-Vendor Marketplace Project
-- This script creates the necessary database and user for the development environment.

-- Create the development database
CREATE DATABASE IF NOT EXISTS multi_vendor_marketplace_dev_db;

-- Create a new user for the development database
CREATE USER IF NOT EXISTS 'multi_vendor_marketplace_dev' @'localhost' IDENTIFIED BY 'multi_vendor_marketplace_dev_pwd';

-- Grant all privileges on the development database to the new user
GRANT ALL PRIVILEGES ON `multi_vendor_marketplace_dev_db`.* TO 'multi_vendor_marketplace_dev' @'localhost';

-- Allow the user to select on performance schema
GRANT
SELECT
    ON `performance_schema`.* TO 'multi_vendor_marketplace_dev' @'localhost';

-- Apply the changes
FLUSH PRIVILEGES;