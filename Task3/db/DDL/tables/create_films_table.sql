use films_catalog;

drop table if exists films;
create table films
(
    film_id       int           not null
        primary key,
    title         varchar(200)  null,
    year          int(4)        null,
    genres        varchar(100)  null,
    ratings_count int default 0 null,
    ratings_sum   int default 0 null
);