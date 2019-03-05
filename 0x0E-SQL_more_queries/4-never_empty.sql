-- script to create a table in server
-- DDL query to do so
CREATE TABLE IF NOT EXISTS id_not_null(
  id INT DEFAULT 1,
  name VARCHAR(256) NOT NULL
);
