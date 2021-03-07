from mysql import connector

import db_setup.db_connect as conn
from db_setup.config import file_folder_path
import csv


def parse_ratings_csv():
    try:
        with open(file_folder_path + '/data/ml-latest-small/ratings.csv', newline='') as ratings:
            ratings_csv = csv.reader(ratings, delimiter=',', quotechar='"')
            next(ratings)
            cursor = conn.Database().connect()
            #
            cursor.execute('use films_prepare_catalog;')
            for user_id, movie_id, rating, timestamp in ratings_csv:
                try:
                    cursor.execute(
                        "INSERT INTO films_prepare_catalog.ratings(movie_id, user_id, rating, `timestamp`) VALUES (%(movie_id)s,%(user_id)s,%(rating)s,%(timestamp)s);",
                        {'user_id': user_id, 'movie_id': movie_id, 'rating': rating, 'timestamp': timestamp})
                    # cnx.commit()
                except connector.Error as e:
                    print('Error while parsing movies.csv', e)
            cnx = conn.Database().get_connection()
            cnx.commit()
    except Exception:
        print('Error while reading movies.csv')


def parse_films_csv():
    try:
        with open(file_folder_path + '/data/ml-latest-small/movies.csv', newline='') as movies:
            movies_csv = csv.reader(movies, delimiter=',', quotechar='"')
            next(movies)
            cursor = conn.Database().connect()
            # cnx = conn.Database().get_connection()
            for movie_id, title, genres in movies_csv:
                try:
                    cursor.execute(
                        "INSERT INTO films_prepare_catalog.films(film_id, title, genres) VALUES (%(film_id)s,%(title)s,%(genres)s);",
                        {'film_id': movie_id, 'title': title, 'genres': genres})

                except connector.Error as e:
                    print('Error while parsing movies.csv', e)
            cnx = conn.Database().get_connection()
            cnx.commit()
    except Exception as e:
        print('Error while reading movies.csv', e)
