use films_catalog;

DROP PROCEDURE IF EXISTS `usp_get_all_genres`;
CREATE PROCEDURE `usp_get_all_genres`(OUT rez VARCHAR(200))
BEGIN
    SET @a := 0;
    SELECT GROUP_CONCAT(DISTINCT
                        REPLACE(REPLACE(SUBSTRING_INDEX(SUBSTRING_INDEX(genre, '|', a.nb), '|', -1), CHAR(13), ''),
                                CHAR(10), '') separator '|') data
    FROM movies,
         (SELECT @a := @a + 1 nb
          FROM movies
          WHERE @a < (SELECT MAX(LENGTH(m1.genre)
              - LENGTH(REPLACE(m1.genre, '|', ''))) + 1 max
                      FROM movies m1)) a
    INTO rez;

END;