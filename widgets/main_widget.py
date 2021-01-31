from PyQt5 import QtWidgets, uic, QtChart, QtCore
from datetime import datetime
from config import UI_MAIN_WINDOW, UI_ERRORS_WINDOW, UI_TIMERS_WINDOW, DESIGN_DIR
import pickle
from datetime import datetime
from model.table_window import TableModel
from abs.templates.spreadsheet import SpreadsheetTemplate
from abs.templates.plotting.qtchart import PieChartConstructor
from abs.qt import MoveableWidget

from widgets.errors_table import ErrorsWindow
from widgets.timers_table import TimersWindow
#from widgets.login_widget import LoginWindow
#from widgets.filters import FiltersWindow
from widgets.bar_chart import BarChart
from widgets.combobox import CheckableComboBox

from data_parser import DataParser

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from = DESIGN_DIR)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MoveableWidget):

    my_timer = 0

    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.user = ('default', 'default', 'default', 1)


        self.parser = DataParser()
        self.users = self.parser.users()
        self.machines = self.parser.machines()

        self.errors_journal.clicked.connect(self.open_errors_table)
        self.timers_journal.clicked.connect(self.open_timers_table)
        self.login_b.clicked.connect(self.open_login_widget)
        self.graph_b.clicked.connect(self.set_up_diagram)
        self.stat_b.mouseReleaseEvent = lambda e : self.stackedWidget.setCurrentIndex(0)

        self.users_box = CheckableComboBox(self)
        self.users_box.addItems(self.users)
        self.users_box.setGeometry(760, 40, 161, 35)
        self.users_box.show()

        self.machines_box =  CheckableComboBox(self)
        self.machines_box.addItems(self.machines)
        self.machines_box.setGeometry(1100, 40, 161, 35)
        self.machines_box.show()
        self.set_filters.clicked.connect(self.set_up_filters)

        #self.filters.clicked.connect(self.open_filters)

    def set_up_filters(self) -> list:

        start_date = self.start_date.date().toPyDate()
        start_time = self.start_time.time().toPyTime()
        start_datetime = datetime.combine(start_date, start_time)
        start_datetime_to_str = datetime.strftime(start_datetime, '%Y-%m-%d %H:%M:%S')


        finish_date = self.finish_date.date().toPyDate()
        finish_time = self.finish_time.time().toPyTime()
        finish_datetime = datetime.combine(finish_date, finish_time)
        finish_datetime_to_str = datetime.strftime(finish_datetime, '%Y-%m-%d %H:%M:%S')

        users = self.users_box.currentData()
        equipment = self.machines_box.currentData()


        return start_datetime_to_str, finish_datetime_to_str, users, equipment



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

    def set_up_diagram(self):

        clearLayout(self.graph_place)
        self.stackedWidget.setCurrentIndex(1)
        self.graph_place.addWidget(BarChart())


    def open_filters(self):

        self.filters = FiltersWindow(self.users_db, self.machines_db)
        self.filters.show()

    def update_timer(self):

        self.setItem(0, 0, QtWidgets.QTableWidgetItem(str(my_timer)))

    def exp_to_xlsx():

        pass

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


    def filters(self):
        pass



    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()


def clearLayout(layout):

  while layout.count():

    child = layout.takeAt(0)

    if child.widget():

      child.widget().deleteLater()


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
