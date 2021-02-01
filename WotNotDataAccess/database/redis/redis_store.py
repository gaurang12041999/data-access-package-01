from WotNotDataAccess.database.redis.conn_redis import connect as redis_connect


def get_json(authenticator, redis_conn, key):
    redis_conn = redis_connect(authenticator) if not redis_conn else redis_conn
    return redis_conn.execute_command('JSON.GET', key, '.')


def set_json(authenticator, redis_conn, key, value, path='.'):
    redis_conn = redis_connect(authenticator) if not redis_conn else redis_conn
    redis_conn.execute_command('JSON.SET', key, path, value)

