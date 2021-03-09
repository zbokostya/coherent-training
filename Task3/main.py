import pathlib
import argparse
import db_setup.db_connect as conn
import time
import db_setup.csv_parser as csv

from db_setup.config import file_folder_path

scripts_rez = [
    'db/DDL/tables/create_films_table.sql',
    'db/DML/insert/insert_refactored_films.sql',
    'db/DDL/tables/create_filtered_table.sql',
    'db/DDL/procedures/get_genres_string.sql',
    'db/DDL/procedures/get_top_films_by_filters.sql',
]

scripts_prepare = [
    'db/DDL/tables/create_prepare_ratings_table.sql',
    'db/DDL/tables/create_prepare_films_table.sql',
]


def parse_arg():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=10, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-to_csv', action="store_false", help="Print result to csv")
    return parser.parse_args()


def run_scripts(scripts):
    for script in scripts:
        script_path = file_folder_path / pathlib.Path(script)
        conn.run_script(script_path)


def print_result(cursor):
    print('genre,title,year,rating')
    for i in cursor:
        print("{},{},{},{}".format(i[2], i[0], i[1], i[3]))


def main():
    start = time.time()
    args = parse_arg()
    run_scripts(scripts_prepare)
    csv.parse_films_csv()
    csv.parse_ratings_csv()
    run_scripts(scripts_rez)
    result = conn.get_result(args.genres, args.year_from, args.year_to, args.regexp, args.N)
    print_result(result)
    print(time.time() - start)


if __name__ == '__main__':
    main()
