from WotNotDataAccess.database.mysql.conn_mysql import DatabaseHandler
from WotNotDataAccess.utility.authentication import get_config


def execute_fetch_all(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        return cursor.fetchall()


def fetch_all(config, conn, sql_stmt, params=None):
    config = get_config(config)
    if conn:
        return execute_fetch_all(conn, sql_stmt, params)

    with DatabaseHandler(config) as conn:
        return execute_fetch_all(conn, sql_stmt, params)
