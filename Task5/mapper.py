import argparse
import re
import sys


class Mapper:
    def __init__(self, year_from, year_to, regexp, genres):
        self.year_from = year_from
        self.year_to = year_to
        self.regexp = regexp
        self.genres = genres

    def map(self, line_num, line):
        _, title, genres = split_line(line)
        year, year_index = parse_year(title)
        title = title[0:year_index - 1]
        if self.genres != ['']:
            for genre in self.genres:
                if self.year_from <= year <= self.year_to and re.search(self.regexp, title):
                    if genre.lower() in genres.lower():
                        yield genre, (title, year)
        else:
            if self.year_from <= year <= self.year_to and re.search(self.regexp, title):
                for genre in genres.split(sep='|'):
                    yield genre, (title, year)


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
           line[line.find(',') + 1:line.rfind(',') - 1].replace('"', ''), \
           line[line.rfind(',') + 1:len(line) - 1].replace('\r', '')


def split_genres(genres):
    return genres.split(sep=',')


def parse_arg():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=-1, type=int, help='Number of max rating movies')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')

    return parser.parse_args()


def main():
    args = parse_arg()

    mapper = Mapper(args.year_from, args.year_to, args.regexp, split_genres(args.genres))

    for i, line in enumerate(sys.stdin):
        for val in mapper.map(i, line):
            print("{}\t{}".format(val[0], val[1]))


if __name__ == '__main__':
    main()
