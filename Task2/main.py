import csv
import argparse
import time
import logging

DATA_DIR = 'data/ml-latest-small/'


def get_films_id_by_genres_year(genres, year_from, year_to):
    with open(DATA_DIR + 'movies.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        films = []
        for row in spamreader:
            for genre in genres:
                year_index = row[1].rfind('(')
                try:
                    if genre in row[2] and year_from <= int(row[1][year_index + 1:year_index + 5]) <= year_to:
                        films.append(row[0])
                        break
                except ValueError:
                    logging.error(row)
                    continue
        return films


def count_ratings(films, count_n):
    ratings = dict()
    for film in films:
        ratings[film] = [0.0, 0]
    with open(DATA_DIR + 'ratings.csv', newline='') as csvfile2:
        spamreader = csv.reader(csvfile2, delimiter=',', quotechar='"')
        for row in spamreader:
            if row[1] in ratings:
                try:
                    ratings[row[1]] = [ratings[row[1]][0] + float(row[2]), ratings[row[1]][1] + 1]
                except ValueError as e:
                    print(e)
                    continue
        for el in ratings:
            if ratings[el][1] != 0:
                ratings[el] = ratings[el][0] / ratings[el][1]
            else:
                ratings[el] = 0
        return dict(sorted(ratings.items(), key=lambda item: item[1], reverse=True)[:count_n])


def arg_parse():
    # tofix
    parser = argparse.ArgumentParser(description='Abc')
    parser.add_argument('-N', default=10, type=int, help='')
    parser.add_argument('-genres', default='', type=str, help='')
    parser.add_argument('-year_from', default=0, type=int, help='')
    parser.add_argument('-year_to', default=9999, type=int, help='')
    parser.add_argument('-regexp', default='', type=str, help='')
    return parser.parse_args()


def parse_films_genres(films_arg):
    return films_arg.split(sep='|')


def create_csv_like_format(top_ratings):
    print('genre, title, year, rating')

    with open(DATA_DIR + 'movies.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        films = []
        for row in spamreader:
            if row[0] in top_ratings:
                print((row[2], row[1], top_ratings[row[0]]))
                films.append((row[2], row[1], top_ratings[row[0]]))
        films = sorted(films, key=lambda item: item[2], reverse=True)
        for film in films:
            print(film)


def main(args):
    genres = parse_films_genres(args.genres)
    films = get_films_id_by_genres_year(genres, args.year_from, args.year_to)
    ratings = count_ratings(films, count_n=args.N)
    create_csv_like_format(ratings)


if __name__ == '__main__':
    start = time.time()
    args = arg_parse()
    main(args)
    print(time.time() - start)
