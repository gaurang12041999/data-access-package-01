import json

from WotNotDataAccess.database.redis import redis_store
from WotNotDataAccess.database.redis.enum import RedisKeyEnum


def get_account_bots_from_redis(config, redis_conn, account_id):
    redis_key = RedisKeyEnum.ACCOUNT_BOTS.value.format(account_id=account_id)
    return redis_store.get_json(config, redis_conn, redis_key)


def set_account_bots_in_redis(config, redis_conn, account_id, payload):
    redis_key = RedisKeyEnum.ACCOUNT_BOTS.value.format(account_id=account_id)
    redis_store.set_json(config, redis_conn, redis_key, json.dumps(payload))
