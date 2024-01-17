-- Prepares a MySQL Test server for the project.

-- Creates a new database named hbnb_test_db if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a new user 'hbnb_test' with the password 'hbnb_test_pwd' if the user doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the hbnb_test_db database to the 'hbnb_test' user when accessing from 'localhost'.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on the performance_schema database to the 'hbnb_test' user when accessing from 'localhost'.
-- The performance_schema is a MySQL system database that provides performance-related information.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

