use films_catalog;

create table if not exists films
(
    film_id       int           not null
        primary key,
    title         varchar(200)  null,
    year          int(4)        null,
    genres        varchar(100)  null,
    ratings_count int default 0 null,
    ratings_sum   int default 0 null
);

truncate table films;