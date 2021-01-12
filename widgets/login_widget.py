from PyQt5 import QtWidgets, uic, QtCore
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget
from storage.login_database import Login_Database

from config import UI_LOGIN_WINDOW, DESIGN_DIR

Ui_LoginWindow, _ = uic.loadUiType(UI_LOGIN_WINDOW, import_from = DESIGN_DIR)

class LoginWindow(QtWidgets.QWidget, Ui_LoginWindow):

    def __init__(self, database: Login_Database, host: QtWidgets.QMainWindow) -> None:

        QtWidgets.QWidget.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.host = host
        self.database = database
        self.submit_button.clicked.connect(self.check_login)
        self.cancel_button.clicked.connect(self.cancel)

    def check_login(self) -> tuple:
       """
       Shows main window if login and password matches data in database
       """
       user_login = self.login_line.text()
       user_password = self.password_line.text()
       if user_login and user_password:
           if self.database.authorization_check(user_login, user_password):
               self.message_info.setText('Авторизация успешна')
               self.hide()
               self.host.show()
               self.user = self.database.authorization_check(user_login, user_password)

           else:
               self.message_info.setStyleSheet("QLabel { border: 1px solid red; border-radius: 5px; background-color: white; }")
               self.message_info.setText('Логин и пароль не найдены')

    def cancel(self):
        self.hide()
        self.host.show()


    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()
