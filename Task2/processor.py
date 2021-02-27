import re
import csv
import logging
from film import Film

logging.basicConfig(format="", level=logging.DEBUG)

DATA_DIR = 'data/ml-latest-small/'


def get_films_id_by_filters(genres, year_from, year_to, regexp):
    try:
        with open(DATA_DIR + 'movies.csv', newline='') as movies:
            films_csv = csv.reader(movies, delimiter=',', quotechar='"')
            films = dict()
            for film_id, film_name, film_genres in films_csv:
                for genre in genres:
                    parse_year = year_parse(film_name)
                    if genre in film_genres and year_from <= parse_year[0] <= year_to and re.search(regexp, film_name):
                        films[film_id] = Film(film_genres, film_name[0:parse_year[1] - 1], parse_year[0])
                        break
        return films
    except Exception:
        logging.error("Error occurred while parsing films")


def year_parse(name):
    year_index = name.rfind('(')
    try:
        year = int(name[year_index + 1:year_index + 5])
    except ValueError:
        year = 0
        year_index = len(name)
    return year, year_index


def count_ratings(films):
    try:
        with open(DATA_DIR + 'ratings.csv', newline='') as ratings_csv:
            rating_csv = csv.reader(ratings_csv, delimiter=',', quotechar='"')
            next(rating_csv, None)
            for _, movie_id, rating, _ in rating_csv:
                if movie_id in films:
                    films[movie_id].rating_sum = films[movie_id].rating_sum + float(rating)
                    films[movie_id].rating_count = films[movie_id].rating_count + 1
            return sorted(films.items(),
                          key=lambda item: item[1].get_rating(),
                          reverse=True)
    except Exception:
        logging.error("Error occurred while counting rating")


def print_csv_like_format(top_ratings, count_n):
    print('genre,title,year,rating')
    for _, film in top_ratings[:count_n]:
        print(film)


def parse_films_genres(films_arg):
    return films_arg.split(sep='|')
