from PyQt5 import QtWidgets, uic, QtChart, QtCore
from datetime import datetime
from config import UI_MAIN_WINDOW, UI_ERRORS_WINDOW, UI_TIMERS_WINDOW, DESIGN_DIR
import pickle
from model.table_window import TableModel
from abs.templates.spreadsheet import SpreadsheetTemplate
from abs.templates.plotting.qtchart import PieChartConstructor
from abs.qt import MoveableWidget

from widgets.errors_table import ErrorsWindow
from widgets.timers_table import TimersWindow
from widgets.login_widget import LoginWindow

from storage.login_database import Login_Database
from storage.timers_database import Timers_Database

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from = DESIGN_DIR)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MoveableWidget):

    my_timer = 0

    def __init__(self, users_db: Login_Database, timers_db: Timers_Database) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.user = ('default', 'default', 'default', 1)
        self.users_db = users_db()
        self.timers_db = timers_db()
        self.errors_journal.clicked.connect(self.open_errors_table)
        self.timers_journal.clicked.connect(self.open_timers_table)
        self.login_b.clicked.connect(self.open_login_widget)
        self.graph_b.mouseReleaseEvent = lambda e : self.stackedWidget.setCurrentIndex(1)
        self.stat_b.mouseReleaseEvent = lambda e : self.stackedWidget.setCurrentIndex(0)


    def open_errors_table(self):

        self.errors_table = ErrorsWindow()
        self.errors_table.show()

    def open_login_widget(self):

        self.login_widget = LoginWindow(self.users_db, self)
        self.login_widget.show()
        self.login_widget.submit_button.clicked.connect(self.click_check)

    def click_check(self):

        self.user = self.login_widget.user


    def open_timers_table(self):

        self.timers_table = TimersWindow(self.timers_db)
        self.timers_table.user = self.user
        print(self.user)
        self.timers_table.show()

    def update_timer(self):

        self.setItem(0, 0, QtWidgets.QTableWidgetItem(str(my_timer)))

    def exp_to_xlsx():
        
    #def create_table(self, table_template, test_data):

        table_widget = table_template
        table_widget.setRowCount(5)
        table_widget.setColumnCount(3)
        table_widget.setCurrentCell(0, 0)

        table_widget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Параметр'))
        table_widget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Время, сек'))
        table_widget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Относительное время, %'))

        table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem('Работа программы'))
        table_widget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(test_data['Program_total_abs'])))

        table_widget.setItem(1, 0, QtWidgets.QTableWidgetItem('Выполнение задачи'))
        table_widget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(test_data['Task_total_abs'])))

        table_widget.setItem(2, 0, QtWidgets.QTableWidgetItem('Работа лазера'))
        table_widget.setItem(2, 1, QtWidgets.QTableWidgetItem(str(test_data['Laser_total_abs'])))

        table_widget.setItem(3, 0, QtWidgets.QTableWidgetItem('Паузы'))
        table_widget.setItem(3, 1, QtWidgets.QTableWidgetItem(str(test_data['Pause_total_abs'])))

        table_widget.setItem(4, 0, QtWidgets.QTableWidgetItem('Газ'))
        table_widget.setItem(4, 1, QtWidgets.QTableWidgetItem(str(test_data['Gas_total_abs'])))

        table_widget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(test_data['Program_total_rel']*100)))

        table_widget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(test_data['Task_total_rel']*100)))

        table_widget.setItem(2, 2, QtWidgets.QTableWidgetItem(str(test_data['Laser_total_rel']*100)))

        table_widget.setItem(3, 2, QtWidgets.QTableWidgetItem(str(test_data['Pause_total_rel']*100)))

        table_widget.setItem(4, 2, QtWidgets.QTableWidgetItem(str(test_data['Gas_total_rel']*100)))

        return table_widget
        #return table_widget


    def create_piechart(self) -> QtChart.QChartView:

        series = QtChart.QPieSeries()

        [series.append (*piece) for piece in [
        ('Лазер',test_data['Laser_total_rel']*100),
        ('Задача',test_data['Task_total_rel']*100),
        ('Паузы',test_data['Pause_total_rel']*100),
        ('Газ',test_data['Gas_total_rel']*100),
        ]]

        pie = PieChartConstructor(series)
        pie.add_slice(0)

        return pie


    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()


def dump_data(main_window):

    data_save = []

    # rowCount() This property holds the number of rows in the table
    for row in range(main_window.table.rowCount()):
        row_data = []
        for column in range(main_window.table.columnCount()):
        # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            item = main_window.table.item(row, column).text()
            row_data.append(item)
            #item = main_window.table.item(row, column).text()
        print(f'row: {row}, column: {column}, row_data={row_data}')
        data_save.append(row_data)
    print(data_save)

    with open('program_data.pkl', 'wb') as f:
        pickle.dump(data_save, f)
