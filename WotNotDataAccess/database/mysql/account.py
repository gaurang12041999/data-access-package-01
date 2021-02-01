from WotNotDataAccess.database.mysql.db_store import fetch_all
from WotNotDataAccess.database.mysql.enum import MysqlQuires


def get_bot_accounts_from_db(authenticator, conn, account_id):
    sql_stmt = MysqlQuires.GET_BOT_ACCOUNTS_FROM_DB.value
    params = {
        'account_id': account_id,
    }
    return fetch_all(authenticator, conn, sql_stmt, params)
