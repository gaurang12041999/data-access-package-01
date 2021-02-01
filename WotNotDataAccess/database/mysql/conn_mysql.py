"""Handle the MySql Database Connection"""
import pymysql

__all__ = ['connect', 'close', 'DatabaseHandler']


def connect(authenticator):
    return pymysql.connect(user=authenticator.config['MYSQL_DATABASE_USER'],
                           password=authenticator.config['MYSQL_DATABASE_PASSWORD'],
                           host=authenticator.config['MYSQL_DATABASE_HOST'],
                           database=authenticator.config['MYSQL_DATABASE_DB'],
                           cursorclass=pymysql.cursors.DictCursor,
                           charset='utf8mb4')


def close(conn):
    if conn is not None and conn.open:
        conn.close()


class DatabaseHandler(object):
    def __init__(self, authenticator):
        self.conn = None
        self.authenticator = authenticator

    def __enter__(self):
        self.conn = connect(self.authenticator)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        close(self.conn)
