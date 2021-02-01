"""Handle the Redis Connection"""
import redis


def connect(authenticator):
    return redis.Redis(host=authenticator.config['REDIS_HOST'],
                       port=authenticator.config['REDIS_PORT'],
                       db=authenticator.config['REDIS_DB'],
                       password=authenticator.config['REDIS_PASSWORD'])
