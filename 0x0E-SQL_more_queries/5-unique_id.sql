-- script to create a table in server
-- DDL query to do so
CREATE TABLE IF NOT EXISTS unique_id(
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256) NOT NULL
);
