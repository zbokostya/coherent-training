from db_setup.config import config
import mysql.connector


def get_connect_to_db():
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except Exception:
        print('Error while connecting to db')
        cnx.close()


def run_script(sql_file_path):
    cnx = get_connect_to_db()
    cursor = cnx.cursor(buffered=True)
    with open(sql_file_path, 'r') as script_file:
        sql_query = script_file.read()
        try:
            cursor.execute(sql_query, multi=True)
            cnx.commit()
        except Exception:
            print("error")


def get_result(genres='', year_from=0, year_to=9999, regexp='', cont_n=10):
    cnx = get_connect_to_db()
    cnx.connect(database='films_catalog')
    cursor = cnx.cursor(buffered=True)
    cursor.callproc('filter', (genres, year_from, year_to, regexp, cont_n))
    cursor.execute('SELECT * FROM filtered_films')
    return cursor.fetchall()

