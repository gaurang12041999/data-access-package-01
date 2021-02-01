import json

from WotNotDataAccess.database.redis.account import get_account_bots_from_redis, set_account_bots_in_redis
from WotNotDataAccess.database.mysql.account import get_bot_accounts_from_db
from WotNotDataAccess.utility.utils import Messenger


class ManageAccount:
    def __init__(self, authenticator, redis_conn=None, db_conn=None):
        self.message = Messenger()
        self.authenticator = authenticator
        self.message.redis_conn = redis_conn
        self.message.db_conn = db_conn

    def get_account_bots_from_account_id(self, account_id):
        self.authenticator.logger.info("It's my log")
        account_bots = get_account_bots_from_redis(self.authenticator, self.message.redis_conn, account_id)
        if account_bots:
            return json.loads(account_bots)
        return SyncAccountBotsInRedis(self.message, self.authenticator).sync_account_bots(account_id)


class SyncAccountBotsInRedis:
    def __init__(self, message, authenticator):
        self.message = message
        self.authenticator = authenticator
        self.message.bots = {"bots": []}

    def sync_account_bots(self, account_id):
        self.message.account_bots = get_bot_accounts_from_db(self.authenticator, self.message.db_conn, account_id)
        if self.message.account_bots:
            self.prepare_account_bots_payload()
            self.set_account_bots_in_redis(account_id)
        return self.message.bots

    def prepare_account_bots_payload(self):
        self.message.bots = {"bots": [bot['id'] for bot in self.message.account_bots]}

    def set_account_bots_in_redis(self, account_id):
        set_account_bots_in_redis(self.authenticator, self.message.redis_conn, account_id, self.message.bots)
