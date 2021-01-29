import json

from WotNotDataAccess.database.redis.account import get_account_bots_from_redis, set_account_bots_in_redis
from WotNotDataAccess.database.mysql.account import get_bot_accounts_from_db


class ManageAccount:
    def __init__(self, config):
        self.config = config

    def get_account_bots_from_account_id(self, account_id):
        account_bots = get_account_bots_from_redis(self.config, account_id)
        if account_bots:
            return json.loads(account_bots)
        return SyncAccountBotsInRedis(self.config).sync_account_bots(account_id)


class SyncAccountBotsInRedis:
    def __init__(self, config):
        self.config = config
        self.account_bots = []

    def sync_account_bots(self, account_id):
        self.account_bots = get_bot_accounts_from_db(self.config, account_id)
        if self.account_bots:
            self.prepare_account_bots_payload()
            self.set_account_bots_in_redis(account_id)
        return self.account_bots

    def prepare_account_bots_payload(self):
        self.account_bots = {"bots": [bot['id'] for bot in self.account_bots]}

    def set_account_bots_in_redis(self, account_id):
        set_account_bots_in_redis(self.config, account_id, self.account_bots)
