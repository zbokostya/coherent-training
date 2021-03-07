use films_prepare_catalog;

create table if not exists films
(
    film_id int          not null,
    title   varchar(200) null,
    genres  varchar(100) null,

    constraint pk_films primary key (film_id)
);

truncate table films;