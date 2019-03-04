-- script to convert db to utf-8 encoding
-- DDL query to do conversion
ALTER TABLE first_table MODIFY name BLOB;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8;
