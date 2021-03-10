use films_prepare_catalog;

LOAD DATA INFILE '/var/films/ml-latest-small/ratings.csv'
    INTO TABLE ratings
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES
    (user_id, movie_id, rating, timestamp);
