-- this is to setup the test database
-- and the user

CREATE DATABASE IF NOT EXITS hbnb_test_db;
CREATE USER IF NOT EXITS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLASH PRIVILEGES;