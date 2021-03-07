use films_prepare_catalog;

create table if not exists ratings
(
    movie_id  int   null,
    user_id   int   null,
    rating    float null,
    `timestamp` int   null,

    constraint pk_rating primary key (movie_id, user_id)
);

truncate table ratings;




