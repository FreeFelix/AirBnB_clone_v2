-- Prepares a MySQL server for the project.

-- Creates a new database named hbnb_dev_db if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a new user 'hbnb_dev' with the password 'hbnb_dev_pwd' if the user doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges on the hbnb_dev_db database to the 'hbnb_dev' user when accessing from 'localhost'.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants SELECT privilege on the performance_schema database to the 'hbnb_dev' user when accessing from 'localhost'.
-- The performance_schema is a MySQL system database that provides performance-related information.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

