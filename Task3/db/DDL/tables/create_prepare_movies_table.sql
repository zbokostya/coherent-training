use films_prepare_catalog;

drop table if exists movies;
create table movies
(
    movie_id int          not null,
    title    varchar(200) null,
    genres   varchar(100) null,
    constraint pk_films primary key (movie_id)
);