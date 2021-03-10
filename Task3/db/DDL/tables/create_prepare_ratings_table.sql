use films_prepare_catalog;

drop table if exists ratings;
create table ratings
(
    movie_id    int   null,
    user_id     int   null,
    rating      float null,
    `timestamp` int   null,
    index movie_id_index (movie_id),
    constraint pk_rating primary key (movie_id, user_id)
);



