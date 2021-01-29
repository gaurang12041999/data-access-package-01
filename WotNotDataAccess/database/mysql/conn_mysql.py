"""Handle the MySql Database Connection"""
import pymysql

__all__ = ['connect', 'close', 'DatabaseHandler']


def connect(config):
    return pymysql.connect(user=config.mysql_database_user,
                           password=config.mysql_database_password,
                           host=config.mysql_database_host,
                           database=config.mysql_database_db,
                           cursorclass=pymysql.cursors.DictCursor,
                           charset='utf8mb4')


def close(conn):
    if conn is not None and conn.open:
        conn.close()


class DatabaseHandler(object):
    def __init__(self, config):
        self.conn = None
        self.config = config

    def __enter__(self):
        self.conn = connect(self.config)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        close(self.conn)
