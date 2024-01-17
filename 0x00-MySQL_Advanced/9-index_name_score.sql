-- 9-index_name_score.sql
-- Script to create an index idx_name_first_score on the table names and the first letter of name and score

-- Create the index
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
