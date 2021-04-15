from PyQt5 import QtWidgets, uic, QtCore
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget


Ui_LoginWindow, _ = uic.loadUiType(UI_LOGIN_WINDOW, import_from=DESIGN_DIR)


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow, MoveableWidget):

    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.minimize.mouseReleaseEvent = lambda e : self.showMinimized()
        self.exit.mouseReleaseEvent = self.closeEvent
        self.go_to_signup_page.mouseReleaseEvent = lambda e : self.login_stackedWidget.setCurrentIndex(1)
        self.go_to_login_page.mouseReleaseEvent = lambda e : self.login_stackedWidget.setCurrentIndex(0)

    def closeEvent(self, event=None):
        self.close()
