import csv
import argparse
import time
import logging

DATA_DIR = 'data/ml-25m/'


def get_films_id_by_genres_year(genres, year_from, year_to, regexp):
    with open(DATA_DIR + 'movies.csv', newline='') as csvfile:
        films_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
        films = dict()
        for row in films_csv:
            for genre in genres:
                parse_year = year_parse(row[1])

                if genre in row[2] and year_from <= parse_year[0] <= year_to and regexp in row[1]:
                    films[row[0]] = [row[2], row[1][0:parse_year[1]], parse_year[0], [0, 0]]
                    break
        return films

def year_parse(name):
    year_index = name.rfind('(')
    try:
        year = int(name[year_index + 1:year_index + 5])
    except ValueError:
        year = 0
        year_index = len(name)
    return (year, year_index)

def count_ratings(films, count_n):
    with open(DATA_DIR + 'ratings.csv', newline='') as csvfile:
        films_rating_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in films_rating_csv:
            if row[1] in films:
                try:
                    films[row[1]][3] = [films[row[1]][3][0] + float(row[2]), films[row[1]][3][1] + 1]
                except ValueError as e:
                    print(e)
                    continue
        for el in films:
            if films[el][3][1] != 0:
                films[el][3] = films[el][3][0] / films[el][3][1]
            else:
                films[el][3] = 0
        return sorted(films.items(), key=lambda item: item[1][3], reverse=True)[:count_n]


def arg_parse():
    parser = argparse.ArgumentParser(description='Abc')
    parser.add_argument('-N', default=10, type=int, help='')
    parser.add_argument('-genres', default='', type=str, help='')
    parser.add_argument('-year_from', default=-1, type=int, help='')
    parser.add_argument('-year_to', default=9999, type=int, help='')
    parser.add_argument('-regexp', default='', type=str, help='')
    return parser.parse_args()


def parse_films_genres(films_arg):
    return films_arg.split(sep='|')


def create_csv_like_format(top_ratings):
    print('genre, title, year, rating')
    for el in top_ratings:
        # print(top_ratings[el])
        # print(top_ratings[el][0] + ',' + top_ratings[el][1] + ',' + top_ratings[el][2] + ',' + top_ratings[el][3])
        print(el[1][0] + ',' + el[1][1] + ',' + str(el[1][2]) + ',' + str(el[1][3]))


def main(args):
    genres = parse_films_genres(args.genres)
    films = get_films_id_by_genres_year(genres, args.year_from, args.year_to, args.regexp)
    ratings = count_ratings(films, count_n=args.N)
    create_csv_like_format(ratings)


if __name__ == '__main__':
    start = time.time()
    args = arg_parse()
    main(args)
    print(time.time() - start)
