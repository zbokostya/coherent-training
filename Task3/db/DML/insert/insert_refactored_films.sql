INSERT INTO films_catalog.films
SELECT film_id,
       IF(locate('(', reverse(title)) != 0,
          reverse(trim(substring(reverse(title), locate('(', reverse(title)) + 1))), title) as title,
       IF(title regexp '([0-9]{4})', REGEXP_SUBSTR(title, '([0-9]{4})'), 0)                   as year,
       genres,
       (select count(rating)
        FROM films_prepare_catalog.ratings
        WHERE movie_id = t1.film_id
        GROUP BY movie_id
       ),
       (select sum(rating)
        FROM films_prepare_catalog.ratings
        WHERE movie_id = t1.film_id
        GROUP BY movie_id)
FROM films_prepare_catalog.films as t1;

