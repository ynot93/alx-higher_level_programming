-- List all cities of California in hbtn_0d_usa
-- Results sorted in ascending order by cities.id

SET @california_id = (SELECT id FROM states WHERE name = 'California');

SELECT * FROM cities WHERE state_id = @california_id
ORDER BY id ASC;
