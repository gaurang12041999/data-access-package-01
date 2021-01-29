This package will help to access WotNot data from redis and mysql

**Install**

You can install it with pip:

### pip install git+https://github.com/gaurang19990412/data-access-package.git"


**Example code**

from WotNotDataAccess.utility.authentication import get_authentication_object
from WotNotDataAccess.account import ManageAccount


config = get_authentication_object(REDIS_HOST="Your redis host",
                                   REDIS_PORT="Your redis port",
                                   REDIS_DB="Your redis database",
                                   REDIS_PASSWORD="Your reids password",
                                   MYSQL_DATABASE_USER="Your MySQL user",
                                   MYSQL_DATABASE_PASSWORD="Your MySQL user password",
                                   MYSQL_DATABASE_HOST="Your MySQL host",
                                   MYSQL_DATABASE_DB="Your MySQL database")


print(ManageAccount(config).get_account_bots_from_account_id(126))
