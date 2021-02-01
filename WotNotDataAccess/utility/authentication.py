from WotNotDataAccess.utility.utils import Messenger
from WotNotDataAccess.utility.logger import configure_logger


def initialize_authentication_object(**kwargs):
    """"This method is used to create authentication object which can be use while using
    data-WotNotDataAccess-package """

    authenticator = Messenger()
    authenticator.config = create_config(**kwargs)
    configure_logger(authenticator)

    return authenticator


def create_config(**kwargs):
    """
        :param
            REDIS_HOST: Address of host where Redis is running
            REDIS_PORT: Port of Redis database
            REDIS_PORT: Port of Redis database
            REDIS_DB: Redis database whom you want to WotNotDataAccess
            REDIS_PASSWORD: Redis password associated with the given host

            MYSQL_DATABASE_USER: User of the MySQL database
            MYSQL_DATABASE_PASSWORD: MySQL password associated with the user
            MYSQL_DATABASE_HOST: Address of host where MySQL is running
            MYSQL_DATABASE_DB: MySQL database whom you want to WotNotDataAccess

            ENABLE_GRAYLOG: If you want to enalble graylog then set it's value to 1. Default value is 0.
            GL_SERVER : Graylog server
            GL_PORT: Graulog port
            ENVIRONMENT: APP environment. Default it's development

        :return Authentication object
    """
    return {
        "REDIS_HOST": kwargs.get("REDIS_HOST", "25.25.25.25"),
        "REDIS_PORT": int(kwargs.get("REDIS_PORT", 6379)),
        "REDIS_DB": int(kwargs.get("REDIS_DB", 0)),
        "REDIS_PASSWORD": kwargs.get("REDIS_PASSWORD", "xyz"),
        "MYSQL_DATABASE_USER": kwargs.get("MYSQL_DATABASE_USER", "User"),
        "MYSQL_DATABASE_PASSWORD": kwargs.get("MYSQL_DATABASE_PASSWORD", "Password"),
        "MYSQL_DATABASE_HOST": kwargs.get("MYSQL_DATABASE_HOST", "36.36.36.36"),
        "MYSQL_DATABASE_DB": kwargs.get("MYSQL_DATABASE_DB", "DB"),
        "ENABLE_GRAYLOG": kwargs.get("ENABLE_GRAYLOG", 0),
        "GL_SERVER": kwargs.get("GL_SERVER", "localhost"),
        "GL_PORT": int(kwargs.get("GL_PORT", 12201)),
        "ENVIRONMENT": kwargs.get("ENVIRONMENT", "Development"),
    }
