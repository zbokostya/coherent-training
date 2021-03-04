use films_catalog;

LOAD DATA INFILE '/var/films/ml-latest-small/movies.csv'
INTO TABLE films
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(film_id, title, genres);

LOAD DATA INFILE '/var/films/ml-latest-small/ratings.csv'
INTO TABLE ratings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(user_id, movie_id, rating, timestamp);