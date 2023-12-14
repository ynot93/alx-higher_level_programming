-- Create the table force_name with id and name

USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
