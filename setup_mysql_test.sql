-- this script prepares a MySQL server for the project
-- create project testing database with the name : hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user named : hbnb_test with all privileges on the db hbnb_test_db
-- with password : hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privlege for the user hbnb_test on the db
GRANT SELECT ON performance_schema. * TO 'hbnb_test'@'localhost';
FLUSH PRIVILIGES;
-- granting all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILIGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
FLUSH PRIVILIGES;
