-- Create database hbtn_0d_2 and user user_0d_2 with SELECT privileges
-- The user_0d_2 password should be set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
