from PyQt5 import QtWidgets, uic

from config import UI_LOGIN_WINDOW, DESIGN_DIR
from storage.database import Database


Ui_LoginWindow, _ = uic.loadUiType(UI_LOGIN_WINDOW, import_from=DESIGN_DIR)


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):

    def __init__(self, database: Database, host: QtWidgets.QMainWindow) -> None:
        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.database = database
        self.host = host
        self.submit_button.clicked.connect(self.check_login)

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

    def closeEvent(self, event):
        event.accept()
