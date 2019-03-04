-- script to delete all records with terrible scores
-- DML query to modify table
DELETE FROM second_table
 WHERE score <= 5;
