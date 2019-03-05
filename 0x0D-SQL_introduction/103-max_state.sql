-- script to find max temp for each state
-- DML query to do above operation
SELECT state,MAX(value) AS max_temp
 FROM temperatures
 GROUP BY state
 ORDER BY state;
