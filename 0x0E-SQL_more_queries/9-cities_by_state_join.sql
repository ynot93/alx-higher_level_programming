-- List all cities in hbtn_0d_usa
-- The cities id, name and states name should be displayed
-- Results sorted by cities id in ascending order

SELECT cities.id, cities.name, states.name FROM cities
JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
