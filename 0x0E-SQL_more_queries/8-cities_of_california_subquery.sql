-- grab all cities with state id of california (1)
-- DML query to do so
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
