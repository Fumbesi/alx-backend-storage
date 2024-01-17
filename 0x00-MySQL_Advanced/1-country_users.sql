-- 1-country_users.sql
-- Script to create the 'users' table with country enumeration

-- If the table already exists, do nothing
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);

-- Sample data insertion
-- INSERT INTO users (email, name, country) VALUES ('bob@dylan.com', 'Bob', 'US');
-- INSERT INTO users (email, name, country) VALUES ('sylvie@dylan.com', 'Sylvie', 'CO');
-- INSERT INTO users (email, name, country) VALUES ('john@dylan.com', 'John', 'US');
