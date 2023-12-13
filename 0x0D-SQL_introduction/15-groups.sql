-- List the number of the records with the same score
-- result = score & number of records with the score in column number
-- List should be sorted by descending number of records

SELECT score, COUNT(score) as number FROM second_table
GROUP BY score ORDER BY number DESC, score DESC;
