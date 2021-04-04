use films_catalog;

drop table if exists movies;
create table movies
(
    movie_id int             not null,
    title    varchar(200)    null,
    `year`   smallint(4)     null,
    genre    varchar(30)     null,
    ratings  float default 0 null
);
