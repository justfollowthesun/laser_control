from PyQt5 import QtWidgets, uic
import json
from config import UI_MAIN_WINDOW, DESIGN_DIR
from model.table_window import TableModel
# Read more at
# https://doc.bccnsoft.com/docs/PyQt5/designer.html#using-the-generated-code
Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


class login_user_form(QtWidgets.QMainWindow, Ui_MainWindow):
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
    # with open("author_keys.txt") as write_file:
    #     a=json.loads(write_file)
    login='login'
    password='qwerty'

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]
        self.model=TableModel(data)
        self.tableView_2.setModel(self.model)
    def closeEvent(self, event):
        with open("data_file.json", "w") as write_file:
            json.dump(self.model._data, write_file)
        event.accept()
