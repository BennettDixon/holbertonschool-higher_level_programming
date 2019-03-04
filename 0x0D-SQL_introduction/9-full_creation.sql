-- creates a table 'second_table' in DB
-- DDL query to create table if it doesnt exist
CREATE TABLE IF NOT EXISTS second_table
(id INT,
name VARCHAR(256),
score INT);
-- DML query to insert rows into table
INSERT INTO second_table (id, name, score)
 VALUES (1, 'John', 10);
-- DML query to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (2, 'Alex', 3);
-- DML quert to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (3, 'Bob', 14);
-- DML query to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (4, 'George', 8);
