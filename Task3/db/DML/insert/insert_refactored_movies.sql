use films_prepare_catalog;

INSERT INTO films_catalog.movies
WITH RECURSIVE
    cte_split_genres AS (
        SELECT movie_id,
               SUBSTRING_INDEX(genres, '|', 1)                    AS genre,
               IF(LOCATE('|', genres) != 0,
                  SUBSTRING(genres, LOCATE('|', genres) + 1), '') AS remain_genres
        FROM films_prepare_catalog.movies
        UNION ALL
        SELECT movie_id,
               SUBSTRING_INDEX(remain_genres, '|', 1)                           AS genre,
               IF(LOCATE('|', remain_genres) != 0,
                  SUBSTRING(remain_genres, LOCATE('|', remain_genres) + 1), '') AS remain_genres
        FROM cte_split_genres
        WHERE LENGTH(TRIM(remain_genres)) != 0
    ),
    cte_rating AS (
        SELECT movie_id,
               AVG(rating) AS avg_rat
        FROM ratings
        GROUP BY movie_id
    ),
    cte_year_title AS (
        SELECT movie_id,
               IF(locate('(', reverse(title)) != 0,
                  reverse(trim(substring(reverse(title), LOCATE('(', REVERSE(title)) + 1))), title) as title,
               IF(title REGEXP '\\([0-9]{4}\\)',
                  SUBSTRING(REGEXP_SUBSTR(title, '\\([0-9]{4}\\)'), 2, 4),
                  0)                                                                                as year
        FROM movies
    )
SELECT cte_year_title.movie_id,
       cte_year_title.title,
       cte_year_title.year,
       cte_split_genres.genre,
       cte_rating.avg_rat
FROM cte_split_genres
         LEFT JOIN cte_rating
                   ON cte_split_genres.movie_id = cte_rating.movie_id
         LEFT JOIN cte_year_title
                   ON cte_split_genres.movie_id = cte_year_title.movie_id;
