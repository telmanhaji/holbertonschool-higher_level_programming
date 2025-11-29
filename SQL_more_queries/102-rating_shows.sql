-- This script lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_shows.title - rating sum.
-- It sorts results in descending order by the rating.
-- It uses only one SELECT statement.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
