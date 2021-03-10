use films_prepare_catalog;

LOAD DATA INFILE '/var/films/ml-latest-small/movies.csv'
    INTO TABLE movies
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES
    (movie_id, title, genres);