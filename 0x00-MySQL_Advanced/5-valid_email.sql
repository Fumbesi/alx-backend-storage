-- 5-valid_email.sql
-- Script to create a trigger to reset valid_email when email is changed

-- Create the trigger
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
