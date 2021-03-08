use films_prepare_catalog;


LOAD DATA INFILE '/var/films/ml-25m/ratings.csv'
    INTO TABLE ratings
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES
    (movie_id, user_id, rating, timestamp);