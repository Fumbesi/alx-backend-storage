-- 0-uniq_users.sql
-- Script to create the 'users' table

-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);

-- Sample data insertion
-- INSERT INTO users (email, name) VALUES ('bob@dylan.com', 'Bob');
-- INSERT INTO users (email, name) VALUES ('sylvie@dylan.com', 'Sylvie');
