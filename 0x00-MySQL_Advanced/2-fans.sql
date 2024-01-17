-- 2-fans.sql
-- Script to rank country origins of bands by the number of fans

-- Temporary table to store the results
CREATE TEMPORARY TABLE tmp_ranking AS
SELECT
    origin,
    SUM(nb_fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;

-- Output the result
SELECT
    origin,
    nb_fans
FROM
    tmp_ranking;
