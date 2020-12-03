from PyQt5 import QtWidgets, uic, QtCore
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from databasestorage.databaseconnect import Database
from abs.qt import MoveableWidget


Ui_LoginWindow, _ = uic.loadUiType(UI_LOGIN_WINDOW, import_from=DESIGN_DIR)


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow, MoveableWidget):

    def __init__(self, database: Database, host: QtWidgets.QMainWindow) -> None:
        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.database = database
        self.host = host
        self.submit_button.clicked.connect(self.check_login)
        self.minimize.mouseReleaseEvent = lambda e : self.showMinimized()
        self.exit.mouseReleaseEvent = self.closeEvent
        self.go_to_signup_page.mouseReleaseEvent = lambda e : self.login_stackedWidget.setCurrentIndex(1)
        self.go_to_login_page.mouseReleaseEvent = lambda e : self.login_stackedWidget.setCurrentIndex(0)
        self.submit_button_2.clicked.connect(self.sign_up)
        print(database, host)
    def check_login(self) -> None:
        """
        Shows main window if login and password matches data in database
        """
        user_login=self.login_line.text()
        user_password=self.password_line.text()
        if user_login and user_password:
            if self.database.authorization_check(user_login,user_password):
                self.message_info.setText('Авторизация успешна')
                self.hide()
                self.host.show()
            else:
                self.message_info.setStyleSheet("QLabel { border: 1px solid red; border-radius: 5px; background-color: white; }")
                self.message_info.setText('Логин и пароль не найдены')

    def sign_up(self)-> None:
        enter_login=self.login_line_2.text()
        enter_password=self.password_line_21.text()
        check_password=self.password_line_22.text()
        print(self.database)
        if enter_login and enter_password and enter_password == check_password:
            if self.database.signup_check(enter_login):
                print('OK')

    def closeEvent(self, event=None):
        self.close()
