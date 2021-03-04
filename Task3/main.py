import pathlib
import argparse
import db_setup.db_connect as conn
from db_setup.config import file_folder_path

scripts = [
    'db/DDL/databases/create_database.sql',
    'db/DDL/tables/create_ratings_table.sql',
    'db/DDL/tables/create_films_table.sql',
    'db/DML/import_csv/import_films_csv.sql',
    'db/DML/import_csv/import_ratings_csv.sql',
    'db/DML/update/update_films.sql',
    'db/DDL/tables/create_ratings_table.sql',
    'db/DDL/procedures/get_genres_string.sql',
    'db/DDL/procedures/get_top_films_by_filters.sql'
]


def arg_parse():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=10, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-to_csv', action="store_false", help="Print result to csv")
    return parser.parse_args()


def run_scripts():
    for script in scripts:
        script_path = file_folder_path / pathlib.Path(script)
        conn.run_script(script_path)


def main():
    args = arg_parse()
    run_scripts()
    result = conn.execute_script(args.genres, args.year_from, args.year_to, args.regexp, args.N)
    print_result(result)


def print_result(cursor):
    print('genre,title,year,rating')
    for i in cursor:
        print("{},{},{},{}".format(i[2], i[0], i[1], i[3]))


if __name__ == '__main__':
    main()
