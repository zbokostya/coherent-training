use films_catalog;

DROP PROCEDURE IF EXISTS `usp_get_movies_by_filter`;
CREATE PROCEDURE `usp_get_movies_by_filter`(IN filter_genre TEXT,
                                            IN filter_year_from SMALLINT(4),
                                            IN filter_year_to SMALLINT(4),
                                            IN filter_regexp TEXT,
                                            IN filter_count_n INT)
BEGIN

    IF (length(filter_genre) = 0) THEN
        CALL `usp_get_all_genres`(filter_genre);
    END IF;

    SELECT rs.title, rs.year, rs.genre, rs.ratings
    FROM (
             SELECT title,
                    year,
                    genre,
                    ratings,
                    ROW_NUMBER() OVER (PARTITION BY genre ORDER BY ratings DESC ) AS row_count
             FROM movies
             WHERE locate(genre, filter_genre) != 0
               AND `year` BETWEEN filter_year_from AND filter_year_to
               AND title regexp filter_regexp
         ) rs
    where rs.row_count <= filter_count_n;
END;