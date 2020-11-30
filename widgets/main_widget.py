from PyQt5 import QtWidgets, uic
from config import UI_MAIN_WINDOW, DESIGN_DIR
from storage.database import Database
from widgets.login_widget import LoginWindow
from model.table_window import TableModel

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, database: Database) -> None:
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.database = database
        self.login_widget = LoginWindow(self.database,self)
        self.table = TableModel()
        self.main_table.setModel(self.table)
        # self.login_widget.show()
        self.show()

    def closeEvent(self, event) -> None:
        self.database.close()
        event.accept()
