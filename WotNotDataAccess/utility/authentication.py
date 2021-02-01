from WotNotDataAccess.utility.utils import Messenger


def get_authentication_object(**kwargs):
    """"This method is used to create authentication object which can be use while using data-WotNotDataAccess-package
    :param
        REDIS_HOST: Address of host where Redis is running
        REDIS_PORT: Port of Redis database
        REDIS_DB: Redis database whom you want to WotNotDataAccess
        REDIS_PASSWORD: Redis password associated with the given host

        MYSQL_DATABASE_USER: User of the MySQL database
        MYSQL_DATABASE_PASSWORD: MySQL password associated with the user
        MYSQL_DATABASE_HOST: Address of host where MySQL is running
        MYSQL_DATABASE_DB: MySQL database whom you want to WotNotDataAccess

        :return Authentication object
    """

    authentication_object = Messenger()

    # Redis
    authentication_object.redis_host = kwargs.get("REDIS_HOST", "25.25.25.25")
    authentication_object.redis_port = kwargs.get("REDIS_PORT", 6379)
    authentication_object.redis_db = kwargs.get("REDIS_DB", 0)
    authentication_object.redis_password = kwargs.get("REDIS_PASSWORD", "xyz")

    # MySQL
    authentication_object.mysql_database_user = kwargs.get("MYSQL_DATABASE_USER", "User")
    authentication_object.mysql_database_password = kwargs.get("MYSQL_DATABASE_PASSWORD", "Password")
    authentication_object.mysql_database_host = kwargs.get("MYSQL_DATABASE_HOST", "36.36.36.36")
    authentication_object.mysql_database_db = kwargs.get("MYSQL_DATABASE_DB", "DB")

    return authentication_object


def get_config(config):
    if config:
        return config
    return get_authentication_object()
