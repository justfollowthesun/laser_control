from PyQt5 import QtWidgets, uic

from config import UI_MAIN_WINDOW, DESIGN_DIR

# Read more at
# https://doc.bccnsoft.com/docs/PyQt5/designer.html#using-the-generated-code
Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.submit_button.clicked.connect(self.login)

    def login(self):
        user_login = self.login_line.text()
        user_password = self.password_line.text()
        if user_login:
            if user_login == login_form.login:
                if user_password == login_form.password:
                    print('Success')
                    if self.saveme_chbox.isChecked():
                        print('In system')
                else:
                    print('Неправильный пароль')
            else:
                print('Неправильный логин')


class login_form():
    login = 'login'
    password = 'qwerty'
