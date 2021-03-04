from db_setup.config import config
import mysql.connector


def connect_to_db():
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except Exception:
        print('Error while connecting to db')
        cnx.close()


def run_script(sql_file_path):
    cnx = connect_to_db()
    cursor = cnx.cursor(buffered=True)
    script_file = open(sql_file_path)
    sql_query = script_file.read()
    try:
        cursor.execute(sql_query, multi=True)
        cnx.commit()
    except Exception:
        print("error")


def execute_script(genres='', year_from=0, year_to=9999, regexp='', cont_n=10):
    cnx = connect_to_db()
    cnx.connect(database='films_catalog')
    cursor = cnx.cursor(buffered=True)
    cursor.execute('CALL filter(\'{}\', {}, {}, \'{}\', {})'
                   .format(genres, year_from, year_to, regexp, cont_n))
    cursor.execute('SELECT * FROM filtered_films')
    return cursor


