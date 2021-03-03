import mysql.connector
import pathlib
import argparse

scripts = [
    'create_table.sql',
    'import_csv.sql',
    'update_films.sql',
    'get_top_films_by_filters.sql'
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


def get_connection_to_database():
    cnx = mysql.connector.connect(
        user='root',
        password='zFh3gm0BLnwb',
        port='3306',
        host='127.0.0.1')
    return cnx


def run_scripts(cnx):
    file_folder_path = pathlib.Path(__file__).parent / pathlib.Path('sql')
    cursor = cnx.cursor(buffered=True)

    for script in scripts:
        script_path = file_folder_path / pathlib.Path(script)
        script_file = open(script_path)
        sql_query = script_file.read()
        list(cursor.execute(sql_query, multi=True))
        cnx.commit()
    return cursor


def main():
    args = arg_parse()
    cnx = get_connection_to_database()
    cursor = run_scripts(cnx)
    get_result(cursor, args.genres, args.year_from, args.year_to, args.regexp, args.N)
    print_result(cursor)


def get_result(cursor, genres='', year_from=0, year_to=9999, regexp='', cont_n=10):
    cursor.execute('CALL filter(\'{}\', {}, {}, \'{}\', {})'
                   .format(genres, year_from, year_to, regexp, cont_n))
    cursor.execute('SELECT * FROM cnt')


def print_result(cursor):
    print('genre,title,year,rating')
    for i in cursor:
        print("{},{},{},{}".format(i[2], i[0], i[1], i[3]))


if __name__ == '__main__':
    main()
