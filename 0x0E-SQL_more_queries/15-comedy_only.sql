-- script for selecting TV shows and their genres
-- join statement to do result DML
SELECT
  tv_shows.title AS title
  FROM tv_show_genres
  INNER JOIN tv_shows
  ON tv_show_genres.show_id = tv_shows.id
  INNER JOIN tv_genres
  ON tv_genres.id = tv_show_genres.genre_id
  AND tv_genres.name = 'Comedy'
  ORDER BY title;
