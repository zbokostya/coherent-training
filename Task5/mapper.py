import argparse
import re
import sys


def parse_year(name):
    year_index = name.rfind('(')
    try:
        year = int(name[year_index + 1:year_index + 5])
    except ValueError:
        year = 0
        year_index = len(name)
    return year, year_index


def split_line(line):
    return line[0:line.find(',')], \
           line[line.find(',') + 1:line.rfind(',') - 1].replace('"', ''),\
           line[line.rfind(',') + 1:len(line) - 1]


def split_genres(genres):
    return genres.split(sep=',')


def mapper(line, filter_genres, year_from=0, year_to=9999, regexp=''):
    _, title, genres = split_line(line)
    year, year_index = parse_year(title)
    title = title[0:year_index - 1]
    for genre in filter_genres:
        if year_from <= year <= year_to and re.search(regexp, title):
            if genre.lower() in genres.lower():
                yield genre, (title, year)


def parse_arg():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=-1, type=int, help='Number of max rating movies')
    parser.add_argument('-genres', default='',
                        type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')

    return parser.parse_args()


def main():
    args = parse_arg()
    for line in sys.stdin:
        for key, value in mapper(line, split_genres(args.genres), args.year_from, args.year_to, args.regexp):
            print("{0}\t{1}".format(key, value))


if __name__ == '__main__':
    main()
