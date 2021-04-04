from mysql import connector

import db_admin.db_connect as conn
from db_admin.user_config import file_folder_path
import csv


def get_line_ratings_generator(ratings_csv):
    for user_id, movie_id, rating, timestamp in ratings_csv:
        yield user_id, movie_id, rating, timestamp


def get_line_movies_generator(ratings_csv):
    for movie_id, title, genres in ratings_csv:
        yield movie_id, title, genres


def parse_ratings_csv():
    path_file = file_folder_path + '/data/ml-latest-small/ratings.csv'
    cursor = conn.Database().connect()
    with open(path_file) as ratings:
        ratings_csv = csv.reader(ratings, delimiter=',', quotechar='"')
        next(ratings)

        gen = get_line_ratings_generator(ratings_csv)

        while True:
            chunk = []
            try:
                for _ in range(1_000):
                    chunk.append(next(gen))
                cursor.executemany(
                    "INSERT INTO films_prepare_catalog.ratings(user_id, movie_id, rating, `timestamp`) VALUES (%s,%s,%s,%s);",
                    chunk)
            except StopIteration:
                print(len(chunk))
                cursor.executemany(
                    "INSERT INTO films_prepare_catalog.ratings(user_id, movie_id, rating, `timestamp`) VALUES (%s,%s,%s,%s);",
                    chunk)
                break
        cnx = conn.Database().connection
        cnx.commit()


def parse_movies_csv():
    path_file = file_folder_path + '/data/ml-latest-small/movies.csv'
    cursor = conn.Database().connect()
    with open(path_file) as movies:
        movies_csv = csv.reader(movies, delimiter=',', quotechar='"')
        next(movies)

        gen = get_line_movies_generator(movies_csv)

        while True:
            chunk = []
            try:
                for _ in range(1_000):
                    chunk.append(next(gen))
                cursor.executemany(
                    "INSERT INTO films_prepare_catalog.movies(movie_id, title, genres) VALUES (%s,%s,%s);",
                    chunk)
            except StopIteration:
                print(len(chunk))
                cursor.executemany(
                    "INSERT INTO films_prepare_catalog.movies(movie_id, title, genres) VALUES (%s,%s,%s);",
                    chunk)
                break
        cnx = conn.Database().connection
        cnx.commit()
