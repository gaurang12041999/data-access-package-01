from WotNotDataAccess.database.mysql.conn_mysql import DatabaseHandler


def execute_fetch_all(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        return cursor.fetchall()


def fetch_all(authenticator, conn, sql_stmt, params=None):
    if conn:
        return execute_fetch_all(conn, sql_stmt, params)

    with DatabaseHandler(authenticator) as conn:
        return execute_fetch_all(conn, sql_stmt, params)
