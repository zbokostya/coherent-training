use films_catalog;

create table if not exists films
(
    film_id       int           not null,
    title         varchar(200)  null,
    year          smallint(4)        null,
    genres        varchar(100)  null,
    ratings_count int default 0 null,
    ratings_sum   int default 0 null,

     constraint pk_films primary key (film_id)
);

truncate table films;