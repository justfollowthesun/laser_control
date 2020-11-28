from PyQt5 import QtWidgets, uic

from config import UI_LOGIN_WINDOW, DESIGN_DIR
from databasestorage.databaseconnect import Database


Ui_LoginWindow, _ = uic.loadUiType(UI_LOGIN_WINDOW, import_from=DESIGN_DIR)


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):

    def __init__(self, database: Database):
        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.database = database

    def closeEvent(self, event):
        event.accept()
