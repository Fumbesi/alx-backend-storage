-- 10-div.sql
-- Script to create a function SafeDiv

-- Drop the function if it exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,4)
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
