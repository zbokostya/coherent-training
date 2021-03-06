use films_catalog;

DROP PROCEDURE IF EXISTS `get_all_genres`;
CREATE PROCEDURE `get_all_genres`(OUT rez VARCHAR(200))
BEGIN
    SET @a := 0;
    SELECT GROUP_CONCAT(DISTINCT
                        REPLACE(REPLACE(SUBSTRING_INDEX(SUBSTRING_INDEX(genres, '|', a.nb), '|', -1), CHAR(13), ''),
                                CHAR(10), '') separator '|') data
    FROM films,
         (SELECT @a := @a + 1 nb
          FROM films
          WHERE @a < (SELECT MAX(LENGTH(m1.genres)
              - LENGTH(REPLACE(m1.genres, '|', ''))) + 1 max
                      FROM films m1)) a
    INTO rez;

END;