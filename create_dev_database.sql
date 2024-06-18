-- create_dev_database.sql

CREATE DATABASE airbnb_dev_db;
CREATE USER 'airbnb_dev'@'localhost' IDENTIFIED BY 'airbnb_dev_pwd';
GRANT ALL PRIVILEGES ON airbnb_dev_db.* TO 'airbnb_dev'@'localhost';
FLUSH PRIVILEGES;
