# -*- coding: utf-8 -*-

import logging
import logging.handlers
import config


class Logger(object):
    """Docstring for Logger. """

    def __init__(self, isdebug=True):
        LOG_NAME = config.general_config.get('project_name')
        LOG_FILE = '%s.log' % LOG_NAME
        if isdebug:
            handler = logging.StreamHandler()
        else:
            handler = logging.handlers.RotatingFileHandler(
                LOG_FILE, maxByte=1024 * 1024, backupCount=5)
        fmt = '[%(asctime)s]->%(message)s'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(LOG_NAME)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)
