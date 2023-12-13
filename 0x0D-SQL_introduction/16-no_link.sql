-- List all records of the table second_table
-- Don't list records without a name value
-- Results should display score and name in descending score

SELECT score, name FROM second_table
WHERE NAME IS NOT NULL ORDER BY score DESC;
