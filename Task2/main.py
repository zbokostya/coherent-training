import csv
import argparse
import time
import film

DATA_DIR = 'data/ml-25m/'


def get_films_id_by_genres_year(genres, year_from, year_to, regexp):
    with open(DATA_DIR + 'movies.csv', newline='') as movies:
        films_csv = csv.reader(movies, delimiter=',', quotechar='"')
        films = dict()
        for row in films_csv:
            for genre in genres:
                parse_year = year_parse(row[1])
                if genre in row[2] and year_from <= parse_year[0] <= year_to and regexp in row[1]:
                    films[row[0]] = film.Film(row[2], row[1][0:parse_year[1] - 1], parse_year[0])
                    break
        return films


def year_parse(name):
    year_index = name.rfind('(')
    try:
        year = int(name[year_index + 1:year_index + 5])
    except ValueError:
        year = 0
        year_index = len(name)
    return year, year_index


def count_ratings(films):
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


def arg_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-N', default=10, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    return parser.parse_args()


def parse_films_genres(films_arg):
    return films_arg.split(sep='|')


def create_csv_like_format(top_ratings, count_n):
    result = 'genre, title, year, rating\n'
    for el in top_ratings[:count_n]:
        result = result + el[1].genre + ',' + el[1].name + ',' + str(el[1].year) \
                 + ',' + str("{:.2f}".format(el[1].get_rating())) + '\n'
    return result


def main(args):
    genres = parse_films_genres(args.genres)
    films = get_films_id_by_genres_year(genres, args.year_from, args.year_to, args.regexp)
    ratings = count_ratings(films)
    result = create_csv_like_format(ratings, count_n=args.N)
    print(result)


if __name__ == '__main__':
    args = arg_parse()
    main(args)
