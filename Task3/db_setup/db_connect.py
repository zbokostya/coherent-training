from db_setup.config import config
import mysql.connector as connector


class DataBaseConnection(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DataBaseConnection, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=DataBaseConnection):
    connection = None

    def connect(self):
        try:
            if self.connection is None:
                self.connection = connector.connect(**config)
                self.cursorobj = self.connection.cursor()
            return self.cursorobj
        except Exception:
            print('Error while connecting to db')

    def commit(self):
        if self.connection is not None:
            self.connection.commit()


def run_script(sql_file_path):
    cursor = Database().connect()
    with open(sql_file_path) as script_file:
        print(sql_file_path)
        sql_query = script_file.read()
        try:
            list(cursor.execute(sql_query, multi=True))
        except Exception as e:
            print(e)


def get_result(genres='', year_from=0, year_to=9999, regexp='', cont_n=10):
    cursor = Database().connect()
    cursor.execute('use films_catalog;')
    cursor.callproc('filter', (genres, year_from, year_to, regexp, cont_n))
    cursor.execute('SELECT * FROM filtered_films')
    return cursor.fetchall()
