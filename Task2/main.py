import argparse
import processor


def arg_parse():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=3, type=int, help='Number of max rating movies')
    parser.add_argument('-genres', default='',
                        type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-dataset', default='', type=str, help='Dataset folder')
    return parser.parse_args()


def main():
    args = arg_parse()
    if args.genres == '':
        genres = processor.get_all_genres(args.dataset)
    else:
        genres = processor.parse_movies_genres(args.genres)

    ratings = processor.count_ratings(args.dataset)
    films = processor.get_movies_by_filters(genres, ratings, args.year_from, args.year_to, args.regexp,
                                            args.dataset)
    processor.print_csv_like_format(films, args.N)


if __name__ == '__main__':
    main()
