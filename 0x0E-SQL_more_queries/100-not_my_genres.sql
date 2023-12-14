-- List all genres not linked to the show Dexter
-- Each record should display: tv_genres.name in ascending order

SELECT tv_genres.name FROM tv_genres
LEFT JOIN (
	SELECT tv_show_genres.genre_id
	FROM tv_shows
	JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
) AS linked_genres ON tv_genres.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
