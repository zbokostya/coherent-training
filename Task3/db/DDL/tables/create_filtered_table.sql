use films_catalog;

DROP TABLE IF EXISTS filtered_films;
create table filtered_films
(
    title  varchar(200) null,
    year   int(4)       null,
    genres varchar(100) null,
    rating float        null
);
