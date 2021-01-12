from PyQt5 import QtWidgets, uic, QtCore
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget
from config import UI_TIMERS_WINDOW
from datetime import datetime
from config import DB_TIMERS_PATH, DB_DIR
from storage.timers_database import Timers_Database

Ui_TimersWindow, _ = uic.loadUiType(UI_TIMERS_WINDOW, import_from = DESIGN_DIR)

class TimersWindow(QtWidgets.QWidget, Ui_TimersWindow):

    connection = None

    def __init__(self, database: Timers_Database) -> None:

        QtWidgets.QWidget.__init__(self)
        Ui_TimersWindow.__init__(self)
        self.setupUi(self)
        self.timers_db = Timers_Database()
        self.operation_1.setText(self.timers_db.select_data('operation_1'))
        self.operation_1_reset.clicked.connect(self.reset_timers)

    def reset_timers(self):

        if self.user[3] == 1:

            self.operation_1.setText(self.timers_db.reset_timer_data('operation_1'))
            self.operation_1.setText(self.timers_db.select_data('operation_1'))

    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()
