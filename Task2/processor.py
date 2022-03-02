import re
import csv
import logging
import heapq
from movie import Movie

logging.basicConfig(format="", level=logging.DEBUG)


def get_movies_by_filters(genres, ratings_dict, year_from, year_to, regexp, data_folder):
    try:
        with open(data_folder + '/movies.csv', newline='') as movies:
            movies_csv = csv.reader(movies, delimiter=',', quotechar='"')
            genres_movies = dict()
            for genre in genres:
                genres_movies[genre] = []

            for movie_id, movie_name, movie_genres in movies_csv:
                parse_year = year_parse(movie_name)
                if year_from <= parse_year[0] <= year_to and re.search(regexp, movie_name):
                    for genre in genres:
                        if genre in movie_genres:
                            if movie_id in ratings_dict:
                                rating = ratings_dict[movie_id][0] / ratings_dict[movie_id][1]
                            else:
                                rating = 0.0
                            heapq.heappush(
                                genres_movies[genre],
                                Movie(genre, movie_name[0:parse_year[1] - 1], parse_year[0],
                                      rating))
        return genres_movies
    except FileNotFoundError:
        logging.error("processor:get_movies_by_filters:No such file:" + data_folder + '/movies.csv')
    except Exception:
        logging.error("processor:get_movies_by_filters:Error occurred while parsing movies")


def year_parse(name):
    year_index = name.rfind('(')
    try:
        year = int(name[year_index + 1:year_index + 5])
    except ValueError:
        year = 0
        year_index = len(name)
    return year, year_index


def count_ratings(data_folder):
    ratings_dict = dict()
    try:
        with open(data_folder + '/ratings.csv', newline='') as ratings_csv:
            rating_csv = csv.reader(ratings_csv, delimiter=',', quotechar='"')
            next(rating_csv)
            for _, movie_id, rating, _ in rating_csv:
                if movie_id not in ratings_dict:
                    ratings_dict[movie_id] = (0, 0)
                ratings_dict[movie_id] = (ratings_dict[movie_id][0] + float(rating), ratings_dict[movie_id][1] + 1)
            return ratings_dict
    except FileNotFoundError:
        logging.error("processor:get_movies_by_filters:No such file:" + data_folder + '/ratings.csv')
    except Exception:
        logging.error("processor:count_ratings:Error occurred while counting rating")


def print_csv_like_format(top_ratings, count_n):
    print('genre,title,year,rating')
    for key, value in top_ratings.items():
        arr = heapq.nlargest(count_n, value)
        for i in arr:
            print(i)


def parse_movies_genres(movies_arg):
    return movies_arg.split(sep='|')


def get_all_genres(data_folder):
    try:
        genres = set()
        with open(data_folder + '/movies.csv', newline='') as movies:
            movies_csv = csv.reader(movies, delimiter=',', quotechar='"')
            next(movies)
            for _, _, movie_genres in movies_csv:
                for genre in parse_movies_genres(movie_genres):
                    genres.add(genre)
        return genres
    except Exception as e:
        print(e)
