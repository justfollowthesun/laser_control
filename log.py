import sys
import logging
import os
import time

from logging.handlers import RotatingFileHandler

from config import DEBUG

level = logging.DEBUG if DEBUG else logging.ERROR
#
logger = logging.getLogger("LASER")
logger.setLevel(logging.DEBUG)

if not os.path.exists('logs'):
    os.mkdir('logs')

logfile_name = os.path.join('logs', time.strftime("%d_%m_%Y_%H_%M_%S") + '.log')

fileLog = RotatingFileHandler(logfile_name, mode='w', maxBytes=50*1024*1024,
                              backupCount=5,encoding = 'utf-8', delay=False)

#fileLog = logging.FileHandler('logs\.log',mode='w')
fileLog.setLevel(logging.DEBUG)

consoleLog = logging.StreamHandler()
consoleLog.setLevel(level)

logfile_nameFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logConsoleFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileLog.setFormatter(logfile_nameFormat)
consoleLog.setFormatter(logConsoleFormat)

logger.addHandler(fileLog)
logger.addHandler(consoleLog)


def handle_unhandled_exception(exc_type, exc_value, exc_traceback, thread_identifier=None):
    """Handler for unhandled exceptions that will write to the logs"""
    if issubclass(exc_type, KeyboardInterrupt):
        # call the default excepthook saved at __excepthook__
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    if thread_identifier:
        logger.critical(f"Unhandled exception in {thread_identifier}", exc_info=(exc_type, exc_value, exc_traceback))
    else:
        logger.critical(f"Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_unhandled_exception
