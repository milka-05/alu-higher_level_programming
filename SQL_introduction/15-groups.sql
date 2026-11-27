-- List scores and record counts in second_table ordered by count descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
