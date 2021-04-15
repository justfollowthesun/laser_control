import logging
import os
import log
import sys
import yaml
import platform
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication

def initate_application() -> None:

    """Application entry point."""
    from storage.database import Database
    from widgets.login_widget import LoginWindow
    from widgets.main_widget import MainWindow
    from model.table_window import TableModel
    from data_aggregate import data_aggregate
    from abs.templates.spreadsheet import SpreadsheetTemplate
    from abs.templates.plotting.qtchart import PieChartConstructor
    from utils.input_data_imit import generate_data_flow_generator
    from utils.win import set_current_process_explicit_attributes
    from abs.qt import MoveableWidget

    #from data_aggregate import data4user

    if platform.system() == 'Windows':
        set_current_process_explicit_attributes()

    logger = logging.getLogger(f"LASER.{__name__}")
    logger.warning('str')

    test_data = data_aggregate()
    main_widget = MainWindow(test_data.output_data())
    login_widget = LoginWindow()

    #launch_login_widget(login_widget)
    main_widget.show()
    app.exec_()

def launch_login_widget(login_widget):
    login_widget.show()
    login_widget.submit_button.mouseReleaseEvent = lambda e : login_check(login_widget, database)
    login_widget.submit_button_2.mouseReleaseEvent = lambda e : sign_up(login_widget, database)

def login_check(login_widget, database):

    login = login_widget.login_line.text()
    password = login_widget.password_line.text()

    if login and password:
        if database.authorization_check(login, password):

            login_widget.message_info.setText('Авторизация успешна')
        else:

            login_widget.message_info.setStyleSheet("QLabel { border: 1px solid red; border-radius: 5px; background-color: white; }")
            login_widget.message_info.setText('Логин и пароль не найдены')

def sign_up(login_widget, database):

    enter_login = login_widget.login_line_2.text()
    enter_password = login_widget.password_line_21.text()
    check_password = login_widget.password_line_22.text()

    if enter_login and enter_password and enter_password == check_password:
        if not database.signup_check(enter_login):
            database.add_new_user(enter_login, enter_password)
            login_widget.login_stackedWidget.setCurrentIndex(0)
        else:
            print('Пользователь уже зарегистрирован')

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
