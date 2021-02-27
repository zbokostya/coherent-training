import argparse
import processor


def arg_parse():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=10, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-to_csv', action="store_false", help="Print result to csv")
    return parser.parse_args()


def main(parsed_args):
    genres = processor.parse_films_genres(parsed_args.genres)
    films = processor.get_films_id_by_filters(genres, parsed_args.year_from, parsed_args.year_to, parsed_args.regexp)
    ratings = processor.count_ratings(films)
    processor.print_csv_like_format(ratings, parsed_args.N)


if __name__ == '__main__':
    args = arg_parse()
    main(args)
