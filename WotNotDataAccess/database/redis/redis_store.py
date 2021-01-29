from WotNotDataAccess.database.redis.conn_redis import connect as redis_connect


def get_json(config, key):
    redis_db = redis_connect(config)
    return redis_db.execute_command('JSON.GET', key, '.')


def set_json(config, key, value, path='.'):
    redis_db = redis_connect(config)
    redis_db.execute_command('JSON.SET', key, path, value)

