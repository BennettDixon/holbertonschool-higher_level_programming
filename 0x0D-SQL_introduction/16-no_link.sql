-- lists all records of second_table in DB
-- DML query to show results, filters empty rows
SELECT score, name FROM second_table
 WHERE name != ''
 ORDER BY score DESC;
