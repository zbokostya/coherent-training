use films_catalog;


DROP PROCEDURE IF EXISTS `filter`;
CREATE PROCEDURE `filter`(IN filter_genre TEXT,
                          IN filter_year_from INT(4),
                          IN filter_year_to INT(4),
                          IN filter_regexp TEXT,
                          IN filter_count_n INT)
BEGIN
    DECLARE front TEXT DEFAULT NULL;
    DECLARE frontlen INT DEFAULT NULL;
    DECLARE TempValue TEXT DEFAULT NULL;

    IF (length(filter_genre) = 0) THEN
        CALL `get_all_genres`(filter_genre);
    END IF;
    iterator:
    LOOP
        IF LENGTH(TRIM(filter_genre)) = 0 OR filter_genre IS NULL THEN
            LEAVE iterator;
        END IF;

        SET front = SUBSTRING_INDEX(filter_genre, '|', 1);
        SET frontlen = LENGTH(front);
        SET TempValue = TRIM(front);
        INSERT INTO filtered_films
        SELECT title, year, TempValue, ratings_sum / NULLIF(ratings_count, 0) as rating
        FROM films
        WHERE locate(TempValue, genres) != 0
          and year between filter_year_from and filter_year_to
          and title regexp filter_regexp
        ORDER BY rating DESC
        LIMIT filter_count_n;
        SET filter_genre = INSERT(filter_genre, 1, frontlen + 1, '');
    END LOOP;
end;

