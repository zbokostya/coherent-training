from db_admin.user_config import config
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
                self.connection = connector.connect(**config, autocommit=True)
                self.cursorobj = self.connection.cursor()
            return self.cursorobj
        except connector.Error as e:
            print('Error while connecting to db', e)

    def get_connection(self):
        if self.connection is None:
            self.connect()
        return self.connection


def run_script(sql_file_path):
    cursor = Database().connect()
    cnx = Database().connection
    with open(sql_file_path) as script_file:
        sql_query = script_file.read()
        print(sql_file_path)
        try:
            list(cursor.execute(sql_query, multi=True))
            cnx.commit()
        except connector.Error as e:
            print("Error while executing script: ", sql_file_path)
            print(e)
