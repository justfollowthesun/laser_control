import logging
import os

def initate_application() -> None:
    """Application entry point."""
    import sys
    import platform
    from PyQt5 import QtWidgets
    from widgets.main_widget import MainWindow
    from widgets.login_widget import LoginWindow
    from databasestorage.databaseconnect import Database
    from utils.win import set_current_process_explicit_attributes

    if platform.system() == 'Windows':
        set_current_process_explicit_attributes()

    app = QtWidgets.QApplication(sys.argv)
    db = Database()
    window = MainWindow(db)
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
    initate_application()
