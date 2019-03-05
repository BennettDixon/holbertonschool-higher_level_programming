-- script to create a new user and server
-- DDL query to do so.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- query to grant permissions to new user
GRANT USAGE ON * . * TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
