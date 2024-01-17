-- 8-index_my_names.sql
-- Script to create an index idx_name_first on the table names and the first letter of name

-- Create the index
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
