import logging
import os

from logging.handlers import TimedRotatingFileHandler
from pygelf import GelfUdpHandler
from WotNotDataAccess.utility.utils import make_dir


def configure_logger(authenticator):
    """Set up Logger"""

    if authenticator.config['ENABLE_GRAYLOG']:
        configure_graylog(authenticator)
    else:
        configure_logging_log_file(authenticator)


def configure_graylog(authenticator):
    """Set up Graylog"""

    additional_fields = {
        "app": "wotnot-data-access",
        "facility": "wotnot",
        "environment": authenticator.config['ENVIRONMENT']}

    authenticator.logger = logging.getLogger('WotNot_logger')
    authenticator.logger.setLevel(logging.INFO)

    gelf_upd_handler = GelfUdpHandler(host=authenticator.config["GL_SERVER"],
                                      port=authenticator.config["GL_PORT"],
                                      include_extra_fields=True,
                                      compress=False,
                                      chunk_size=1300,
                                      **additional_fields)

    gelf_upd_handler.debug = True
    gelf_upd_handler.setLevel(logging.INFO)

    authenticator.logger.addHandler(gelf_upd_handler)


def configure_logging_log_file(authenticator):
    """Track Logging in Log file"""

    log_folder_location = os.path.abspath(os.path.join(__file__, '..', '..', 'data', 'logs'))
    make_dir(log_folder_location)

    authenticator.logger = logging.getLogger('WotNot_logger')

    authenticator.logger.setLevel(logging.INFO)

    log_file = '{0}/log'.format(log_folder_location)

    handler = TimedRotatingFileHandler(log_file, when='midnight',
                                       interval=1, encoding='utf8', backupCount=1825)
    handler.setLevel(logging.INFO)

    authenticator.logger.addHandler(handler)

