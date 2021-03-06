use films_catalog;

DROP PROCEDURE IF EXISTS `filter`;
CREATE PROCEDURE `filter`(IN filter_genre TEXT,
                          IN filter_year_from INT(4),
                          IN filter_year_to INT(4),
                          IN filter_regexp TEXT,
                          IN filter_count_n INT)
BEGIN
    DECLARE front TEXT DEFAULT NULL;
    DECLARE cur_genre TEXT DEFAULT NULL;

    IF (length(filter_genre) = 0) THEN
        CALL `get_all_genres`(filter_genre);
    END IF;
    iterator:
    LOOP
        IF LENGTH(TRIM(filter_genre)) = 0 THEN
            LEAVE iterator;
        END IF;

        SET front = SUBSTRING_INDEX(filter_genre, '|', 1);
        SET cur_genre = TRIM(front);
        INSERT INTO filtered_films
        SELECT title, year, cur_genre, ratings_sum / NULLIF(ratings_count, 0) as rating
        FROM films
        WHERE locate(cur_genre, genres) != 0
          and year between filter_year_from and filter_year_to
          and title regexp filter_regexp
        ORDER BY rating DESC
        LIMIT filter_count_n;
        SET filter_genre = INSERT(filter_genre, 1, LENGTH(front) + 1, '');
    END LOOP;
end;

