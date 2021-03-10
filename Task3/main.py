import argparse
from mysql import connector
import db_admin.db_connect as conn


def parse_arg():
    parser = argparse.ArgumentParser(description='Films analytics program')
    parser.add_argument('-N', default=3, type=int, help='Number of max rating films')
    parser.add_argument('-genres', default='', type=str, help='Filter by genres')
    parser.add_argument('-year_from', default=-1, type=int, help='Number of min year to filter')
    parser.add_argument('-year_to', default=9999, type=int, help='Number of max year to filter')
    parser.add_argument('-regexp', default='', type=str, help='Regular expression to filter')
    parser.add_argument('-to_csv', action="store_false", help="Print result to csv")
    return parser.parse_args()


def print_result(cursor):
    print('genre,title,year,rating')
    for el in cursor.stored_results():
        for i in el.fetchall():
            print("{},{},{},{}".format(i[2], i[0], i[1], i[3]))


def get_result(genres='', year_from=-1, year_to=9999, regexp='', cont_n=10):
    cursor = conn.Database().connect()
    try:
        cursor.execute('use films_catalog;')
        cursor.callproc('usp_get_movies_by_filter', (genres, year_from, year_to, regexp, cont_n))
        return cursor
    except connector.Error:
        print("Error while getting result")


def main():
    args = parse_arg()

    result = get_result(args.genres, args.year_from, args.year_to, args.regexp, args.N)
    print_result(result)


if __name__ == '__main__':
    main()
