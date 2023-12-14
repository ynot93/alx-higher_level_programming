-- Create table unique_id with a unique default value 1 of id

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
