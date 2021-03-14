import logging
import os
import log
import sys
import pickle
import yaml
import platform
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication
import psutil

def check_isTimersinsystem() -> None:

    for proc in psutil.process_iter():
    name = proc.name()

    if name == "Timers Journal.exe":
        return True
    else:
        pass

def initate_application() -> None:

    """Application entry point."""

    #from widgets.login_widget import LoginWindow
    from widgets.main_widget import MainWindow
    #from model.table_window import TableModel

    from abs.templates.spreadsheet import SpreadsheetTemplate
    from utils.win import set_current_process_explicit_attributes
    from abs.qt import MoveableWidget

    #from storage.login_database import Login_Database
    #from storage.timers_database import Timers_Database

    #from data_aggregate import data4user

    if platform.system() == 'Windows':
        set_current_process_explicit_attributes()

    logger = logging.getLogger(f"LASER.{__name__}")
    logger.warning('str')

    istimersexist = check_isTimersinsystem()

    if not istimersexist:
        main_widget = MainWindow()
        main_widget.show()
        app.exec_()



def filelog_constructor(*args, **kw) -> logging.FileHandler:
    """
    Called from logging.yml file to set log file path
    """

    import os
    from config import LOG_DIR

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    LOG_FILE = os.path.join(LOG_DIR, 'std_out.log')
    return logging.FileHandler(LOG_FILE)

def setup_logging() -> None:

    import logging.config
    import yaml

    from config import BASE_DIR

    loggingConf = open(os.path.join(BASE_DIR, 'logging.yml'), 'r')
    logging.config.dictConfig(yaml.safe_load(loggingConf))
    loggingConf.close()
    logfile = logging.getLogger('file')
    logconsole = logging.getLogger('console')
    logfile.debug("Debug FILE")
    logconsole.debug("Debug CONSOLE")

    qt_logger = logging.getLogger('PyQt5')
    qt_logger.setLevel(logging.WARNING)

if __name__ == "__main__":
    #setup_logging()

    app = QApplication(sys.argv)
    initate_application()
