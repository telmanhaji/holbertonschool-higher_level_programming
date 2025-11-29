-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- The tv_shows table contains only one record where title = Dexter.
-- Each record displays: tv_genres.name.
-- It sorts results in ascending order by the genre name.
-- It uses maximum of two SELECT statement.
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
