import db_admin.csv_parser as csv
import db_admin.db_connect as conn
import os
from db_admin.user_config import file_folder_path

ddl_scripts_folders = [
    '/db/DDL/databases',
    '/db/DDL/tables'
]

dml_scripts_folders = [
    '/db/DML/insert',
    '/db/DDL/procedures'
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
    run_scripts(ddl_scripts_folders)
    csv.parse_ratings_csv()
    csv.parse_movies_csv()
    run_scripts(dml_scripts_folders)


if __name__ == '__main__':
    main()
