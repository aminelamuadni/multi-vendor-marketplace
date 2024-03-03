-- SQL Setup Script for the Multi-Vendor Marketplace Project
-- This script creates the necessary database and user for the test environment.

-- Create the test database
CREATE DATABASE IF NOT EXISTS multi_vendor_marketplace_test_db;

-- Create a new user for the test database
CREATE USER IF NOT EXISTS 'multi_vendor_marketplace_test' @'localhost' IDENTIFIED BY 'multi_vendor_marketplace_test_pwd';

-- Grant all privileges on the test database to the new user
GRANT ALL PRIVILEGES ON `multi_vendor_marketplace_test_db`.* TO 'multi_vendor_marketplace_test' @'localhost';

-- Allow the user to select on performance schema
GRANT
SELECT
    ON `performance_schema`.* TO 'multi_vendor_marketplace_test' @'localhost';

-- Apply the changes
FLUSH PRIVILEGES;