-- To ensure the script does not fail if the user already exists, it is common to drop the user first,
-- followed by the CREATE USER statement
DROP USER 'user_0d_1'@'localhost';

-- creates user_0d_1 password should be set to user_0d_1_pwd
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grants the user all privileges on the entire MySQL server.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
