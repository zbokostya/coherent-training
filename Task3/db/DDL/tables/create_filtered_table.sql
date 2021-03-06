use films_catalog;

create table if not exists filtered_films
(
    title  varchar(200) null,
    year   int(4)       null,
    genres varchar(100) null,
    rating float        null
);

truncate table filtered_films;
