from enum import Enum


class MysqlQuires(Enum):
    GET_BOT_ACCOUNTS_FROM_DB = "SELECT id from bot_lead where account_id = %(account_id)s"
