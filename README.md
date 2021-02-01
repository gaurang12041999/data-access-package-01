This package will help to access WotNot data from redis and mysql

# Install

You can install it with pip:


`pip install git+https://github.com/gaurang19990412/data-access-package.git`


# Example code

```
from WotNotDataAccess.utility.authentication import initialize_authentication_object
from WotNotDataAccess.account import ManageAccount


authenticator = initialize_authentication_object(REDIS_HOST="Your redis host",
                                   REDIS_PORT="Your redis port",
                                   REDIS_DB="Your redis database",
                                   REDIS_PASSWORD="Your reids password",
                                   MYSQL_DATABASE_USER="Your MySQL user",
                                   MYSQL_DATABASE_PASSWORD="Your MySQL user password",
                                   MYSQL_DATABASE_HOST="Your MySQL host",
                                   MYSQL_DATABASE_DB="Your MySQL database",
                                   ENABLE_GRAYLOG="If you want to enable graylog set value as 1",
                                   GL_SERVER="Your grayplog server",
                                   GL_PORT:"Your graylog port",
                                   ENVIRONMENT: "Environment where you project is running")


print(ManageAccount(authenticator).get_account_bots_from_account_id(126))

```