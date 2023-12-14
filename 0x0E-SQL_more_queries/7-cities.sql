-- Creates database hbtn_0d_usa and table cities
-- The id is unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null, FOREIGN KEY, references id of the states table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
