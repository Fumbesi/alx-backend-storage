-- 11-need_meeting.sql
-- Script to create a view need_meeting

-- Drop the view if it exists
DROP VIEW IF EXISTS need_meeting;

-- Create the view
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80 OR last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
