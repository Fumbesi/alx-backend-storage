-- 101-average_weighted_score.sql
-- Script to create a stored procedure ComputeAverageWeightedScoreForUsers

-- Drop the stored procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_param INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    -- Loop through all users
    users_loop: LOOP
        FETCH cur INTO user_id_param;
        IF done THEN
            LEAVE users_loop;
        END IF;

        -- Call the existing stored procedure ComputeAverageWeightedScoreForUser
        CALL ComputeAverageWeightedScoreForUser(user_id_param);
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;
