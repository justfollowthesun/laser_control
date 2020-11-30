from PyQt5 import QtWidgets, uic, QtCore
from config import UI_MAIN_WINDOW, DESIGN_DIR
from storage.database import Database
from widgets.login_widget import LoginWindow
from model.table_window import TableModel

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#
#     def __init__(self, database: Database) -> None:
#         QtWidgets.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)
#         self.database = database
#         self.login_widget = LoginWindow(self.database,self)
#         self.table = TableModel()
#         self.main_table.setModel(self.table)
#         # self.login_widget.show()
#         self.show()
#
#     def closeEvent(self, event) -> None:
#         self.database.close()
#         event.accept()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.createTable()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.show()

    def update_timer(self):
        """
        Slot that updates date and time values.
        """
        time = QtCore.QTime.currentTime().toString("hh:mm:ss AP")
        self.table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem(time))
        return time

    def createTable(self):
        """
        Set up table widget.
        """
        self.table_widget = QtWidgets.QTableWidget()
        # Set initial row and column values
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(1)
        # Set focus on cell in the table
        self.table_widget.setCurrentCell(0, 0)
        self.setCentralWidget(self.table_widget)
