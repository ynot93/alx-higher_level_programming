-- Create user user_0d_1 who has all privileges
-- Password should be set to user_0d_1_pwd
-- If the user exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
