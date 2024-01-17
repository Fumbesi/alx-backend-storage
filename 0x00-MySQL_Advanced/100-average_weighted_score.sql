-- 100-average_weighted_score.sql
-- Script to create a stored procedure ComputeAverageWeightedScoreForUser

-- Drop the stored procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE average_score FLOAT DEFAULT 0;

    -- Calculate the total weighted score and total weight
    SELECT 
        SUM(corrections.score * projects.weight),
        SUM(projects.weight)
    INTO 
        total_score,
        total_weight
    FROM 
        corrections
    JOIN 
        projects ON corrections.project_id = projects.id
    WHERE 
        corrections.user_id = user_id_param;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    END IF;

    -- Update the average_score in the users table
    UPDATE 
        users 
    SET 
        average_score = average_score 
    WHERE 
        id = user_id_param;
END //

DELIMITER ;

