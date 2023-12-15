-- List all shows displaying tv_shows.title - tv_show_genres.genre_id
-- Sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Display NULL if show doesn't have a genre

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') as genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
