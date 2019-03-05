-- script for selecting TV shows and their genres
-- join statement to do result DML
SELECT
  tv_shows.title AS title,
  tv_genres.name AS name
  FROM tv_show_genres
  RIGHT JOIN tv_shows
  ON tv_show_genres.show_id = tv_shows.id
  LEFT JOIN tv_genres
  ON tv_genres.id = tv_show_genres.genre_id
  ORDER BY title, name;
