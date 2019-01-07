-- Prepares a MySQL server with the database hbnb_dev_db
-- new user hbnb_dev (in localhost)
-- password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on only the database hbnb_dev_db
-- hbnb_dev should have SELECT privilege on only the database performance schema


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
