-- 7-average_score.sql
-- Script to create a stored procedure ComputeAverageScoreForUser

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Compute total score and total projects for the user
    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id_param;

    -- Compute average score and update the users table
    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = user_id_param;
    END IF;
END //

DELIMITER ;
