use films_catalog;

UPDATE films as t1
    inner join (
        select film_id,
               IF(locate(')', reverse(title)) != 0,
                  reverse(substring(reverse(title), locate(')', reverse(title)) + 1, 4)), 0)    as year,
               IF(locate('(', reverse(title)) != 0,
                  reverse(trim(substring(reverse(title), locate('(', reverse(title)) + 1))), 0) as title
        from films
        where film_id
    ) as t2
SET t1.year  = t2.year,
    t1.title = t2.title
where t1.film_id = t2.film_id;

UPDATE films as t1
    inner join (
        select movie_id, count(rating) as cnt, SUM(rating) as sum
        FROM ratings
        GROUP BY movie_id
    ) as t2
SET t1.ratings_count = t2.cnt,
    t1.ratings_sum   = t2.sum
where t1.film_id = t2.movie_id;

