use films_catalog;

drop table if exists ratings;
create table ratings
(
    movie_id  int   null,
    user_id   int   null,
    rating    float null,
    timestamp int   null
);




