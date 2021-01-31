from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLineEdit,QCompleter
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget
from storage.login_database import Login_Database
from config import UI_FILTERS_WINDOW, DESIGN_DIR

from storage.login_database import Login_Database
from storage.timers_database import Timers_Database
from storage.machines_database import Machines_Database

Ui_LoginWindow, _ = uic.loadUiType(UI_FILTERS_WINDOW, import_from = DESIGN_DIR)

test_model_data = ['a', 'b', 'c']

class FiltersWindow(QtWidgets.QWidget, Ui_LoginWindow):

    def __init__(self, user_db: Login_Database, machines_db: Machines_Database) -> None:

        QtWidgets.QWidget.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.user_db = user_db
        self.machines_db = machines_db
        self.users_hint_list = self.user_db.user_col()
        print(self.users_hint_list)
        self.completer = CodeCompleter(self.users_hint_list, self)
        self.user.setCompleter(self.completer)


    def cancel(self):

        self.hide()
        self.host.show()

    def connect_user_db(self, db_name):

        self.user_db



    def closeEvent(self, event) -> None:

        dump_data(self)
        self.close()


class CodeCompleter(QCompleter):

    ConcatenationRole = Qt.UserRole + 1

    def create_model(self, data):

        def addItems(parent, elements, t=""):

            for text, children in elements:

                item = QStandardItem(text)
                data = t + "." + text if t else text
                item.setData(data, CodeCompleter.ConcatenationRole)
                parent.appendRow(item)

                if children:

                    addItems(item, children, data)

        model = QStandardItemModel(self)
        addItems(model, data)
        self.setModel(model)

    # def __init__(self, data, parent=None):
    #     super().__init__(parent)
    #     self.create_model(data)
    #
    # def splitPath(self, path):
    #     return path.split('.')
    #
    # def pathFromIndex(self, ix):
    #     return ix.data(CodeCompleter.ConcatenationRole)
