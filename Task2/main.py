import csv
import argparse
import logging
import re
from film import Film

DATA_DIR = 'data/ml-latest-small/'

logging.basicConfig(format="", level=logging.DEBUG)


def get_films_id_by_filters(genres, year_from, year_to, regexp):
    try:
        with open(DATA_DIR + 'movies.csv', newline='') as movies:
            films_csv = csv.reader(movies, delimiter=',', quotechar='"')
            films = dict()
            for row in films_csv:
                for genre in genres:
                    parse_year = year_parse(row[1])
                    if genre in row[2] and year_from <= parse_year[0] <= year_to and re.search(regexp, row[1]):
                        films[row[0]] = Film(row[2], row[1][0:parse_year[1] - 1], parse_year[0])
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
            for row in rating_csv:
                if row[1] in films:
                    films[row[1]].rating_sum = films[row[1]].rating_sum + float(row[2])
                    films[row[1]].rating_count = films[row[1]].rating_count + 1
            return sorted(films.items(),
                          key=lambda item: item[1].get_rating(),
                          reverse=True)
    except Exception:
        logging.error("Error occurred while counting rating")


def arg_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-N', default=10, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-to_csv', action="store_false", help="Print result to csv")
    return parser.parse_args()


def parse_films_genres(films_arg):
    return films_arg.split(sep='|')


def print_csv_like_format(top_ratings, count_n):
    print('genre,title,year,rating')
    for el in top_ratings[:count_n]:
        print(el[1])


def out_csv(top_ratings, count_n):
    with open(DATA_DIR + 'top.csv', 'w', newline='') as result:
        writer = csv.writer(result, delimiter=',',
                            quotechar='"')
        writer.writerow(['genre', 'title', 'year', 'rating'])
        for el in top_ratings[:count_n]:
            writer.writerow([el[1].genre, el[1].name, el[1].year, el[1].get_rating()])


def main(parsed_args):
    genres = parse_films_genres(parsed_args.genres)
    films = get_films_id_by_filters(genres, parsed_args.year_from, parsed_args.year_to, parsed_args.regexp)
    ratings = count_ratings(films)
    if args.to_csv:
        print_csv_like_format(ratings, parsed_args.N)
    else:
        out_csv(ratings, parsed_args.N)


if __name__ == '__main__':
    args = arg_parse()
    main(args)
