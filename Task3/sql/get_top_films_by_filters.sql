DROP TABLE IF EXISTS cnt;
create table cnt
(
    title  varchar(200) null,
    year   int(4)       null,
    genres varchar(100) null,
    rating float        null
);

# DROP PROCEDURE IF EXISTS get_all_genres;
# CREATE PROCEDURE get_all_genres()
# BEGIN
#     DECLARE ite INT;
#     SET @s = 'INSERT INTO @table1 VALUES (SELECT NULL WHERE 0=1 ';
#     select MAX(LENGTH(genres) - LENGTH(REPLACE(genres, '|', ''))) + 1 as max
#     FROM films
#     INTO ite;
#
#     WHILE (ite > 0)
#         DO
#             SET @s = concat(@s, 'UNION SELECT trim(substring_index(
#                                 SUBSTRING_INDEX(genres, \'|\',' , ite, '),\'|\', -1)) as data
#                              FROM films ');
#             SET ite := ite - 1;
#         END WHILE;
#     SET @s = concat(@s, ');');
#     PREPARE stmt FROM @s;
#     DEALLOCATE PREPARE stmt;
# #     SELECT * from @ table1;
#     INSERT INTO @table1 VALUES (1,2);
#     SELECT * FROM @table1;
#
# END;
# call get_all_genres();



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
