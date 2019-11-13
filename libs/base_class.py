import os
import time
import datetime


class BaseClass:
    import logging
    LOG_LEVEL = logging.INFO
    date = datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y')
    directory = 'logs/%s' % date
    if not os.path.exists(directory):
        os.makedirs(directory)
    logfile = '%s/%s.log' % (directory, datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S'))
    logging.basicConfig(filename=logfile, level=LOG_LEVEL)
    log = logging.getLogger('logger')

    @classmethod
    def log_this(cls, message, is_fatal=False):
        print(message)
        if is_fatal:
            cls.log.fatal(message)
        else:
            cls.log.info(message)
