import csv_parser as csv
import db_connect as conn
import os
from user_config import file_folder_path

scripts_folders = [
    '/db/DDL/databases',
    '/db/DDL/tables',
    '/db/DML/import_csv',
    '/db/DML/insert',
    '/db/DDL/procedure'
]


def run_scripts(folder_path):
    for folder in folder_path:
        try:
            for entry in os.scandir(file_folder_path + folder):
                if entry.is_file():
                    conn.run_script(entry.path)
        except FileNotFoundError:
            print('No such directory: ' + folder)
        except ConnectionError:
            print('Error with connection while executing scripts')


def main():
    run_scripts(scripts_folders)
    # much faster to use 'db/DML/import_csv/' scripts

    # csv.parse_films_csv()
    # csv.parse_ratings_csv()


if __name__ == '__main__':
    main()
