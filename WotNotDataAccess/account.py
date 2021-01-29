import json

from WotNotDataAccess.database.redis.account import get_account_bots_from_redis, set_account_bots_in_redis
from WotNotDataAccess.database.mysql.account import get_bot_accounts_from_db
from WotNotDataAccess.utility.utils import Messenger


class ManageAccount:
    def __init__(self, config, redis_conn=None, db_conn=None):
        self.message = Messenger()
        self.message.config = config
        self.message.redis_conn = redis_conn
        self.message.db_conn = db_conn

    def get_account_bots_from_account_id(self, account_id):
        account_bots = get_account_bots_from_redis(self.message.config, self.message.redis_conn, account_id)
        if account_bots:
            return json.loads(account_bots)
        return SyncAccountBotsInRedis(self.message).sync_account_bots(account_id)


class SyncAccountBotsInRedis:
    def __init__(self, message):
        self.message = message
        self.message.account_bots = []

    def sync_account_bots(self, account_id):
        self.message.account_bots = get_bot_accounts_from_db(self.message.config, self.message.db_conn, account_id)
        if self.message.account_bots:
            self.prepare_account_bots_payload()
            self.set_account_bots_in_redis(account_id)
        return self.message.account_bots

    def prepare_account_bots_payload(self):
        self.message.account_bots = {"bots": [bot['id'] for bot in self.message.account_bots]}

    def set_account_bots_in_redis(self, account_id):
        set_account_bots_in_redis(self.message.config, self.message.redis_conn, account_id, self.message.account_bots)
