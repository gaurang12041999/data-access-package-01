from WotNotDataAccess.database.mysql.conn_mysql import DatabaseHandler


def fetch_all(config, sql_stmt, params=None):
    with DatabaseHandler(config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_stmt, params)
            return cursor.fetchall()
