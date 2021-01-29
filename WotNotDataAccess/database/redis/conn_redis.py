"""Handle the Redis Connection"""
import redis


def connect(config):
    return redis.Redis(host=config.redis_host,
                       port=config.redis_port,
                       db=config.redis_db,
                       password=config.redis_password)
