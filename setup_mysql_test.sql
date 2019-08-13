-- create
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
