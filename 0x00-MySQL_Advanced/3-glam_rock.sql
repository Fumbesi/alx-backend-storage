-- 3-glam_rock.sql
-- Script to list Glam rock bands ranked by longevity

-- Temporary table to store the results
CREATE TEMPORARY TABLE tmp_glam_rock AS
SELECT
    band_name,
    -- Calculate the lifespan using the split and formed attributes
    CASE
        WHEN split = 0 OR formed = 0 THEN 0
        ELSE 2022 - GREATEST(split, formed)
    END AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;

-- Output the result
SELECT
    band_name,
    lifespan
FROM
    tmp_glam_rock;
