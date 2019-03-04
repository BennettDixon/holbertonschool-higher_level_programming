-- script to display number of people with same score
-- DML query using GROUP BY to achieve grouping
SELECT score,COUNT(*) AS 'number' FROM second_table
 GROUP BY score
 ORDER BY score DESC;
