use test1;

DROP TABLE IF EXISTS cnt;
create table cnt
(
    title  varchar(200) null,
    year   int(4)       null,
    genres varchar(100) null,
    rating float        null
);

DROP PROCEDURE IF EXISTS `get_all_genres`;
CREATE PROCEDURE `get_all_genres`(OUT rez VARCHAR(200))
BEGIN
    SET @a := 0;

   SET @a := 0;

SELECT GROUP_CONCAT(DISTINCT REPLACE(REPLACE(SUBSTRING_INDEX(SUBSTRING_INDEX(genres, '|', a.nb), '|', -1), CHAR(13), ''), CHAR(10), '') separator '|') data
                FROM films,
                     (SELECT @a := @a + 1 nb
                      FROM films
                      WHERE @a < (SELECT MAX(LENGTH(m1.genres)
                          - LENGTH(REPLACE(m1.genres, '|', ''))) + 1 max
                                  FROM films m1)) a
    INTO rez;

END;





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

    IF(length(filter_genre) = 0) THEN
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
        INSERT INTO cnt
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

