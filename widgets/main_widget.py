from PyQt5 import QtWidgets, uic, QtChart, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QLabel, QFrame, QGroupBox, QHBoxLayout, QGridLayout, QCalendarWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import *
from datetime import datetime
from config import UI_MAIN_WINDOW, UI_ERRORS_WINDOW, UI_TIMERS_WINDOW, DESIGN_DIR
import pickle
from datetime import datetime
from model.table_window import TableModel
from abs.templates.spreadsheet import SpreadsheetTemplate
from abs.templates.plotting.qtchart import PieChartConstructor
from abs.qt import MoveableWidget
import threading
from widgets.errors_table import ErrorsWindow
from widgets.timers_table import TimersWindow
#from widgets.login_widget import LoginWindow
#from widgets.filters import FiltersWindow
from widgets.bar_chart import BarChart
from widgets.combobox import CheckableComboBox
from storage.timers_database import Timers_Database
from data_parser import DataParser

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from = DESIGN_DIR)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MoveableWidget):

    my_timer = 0

    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.user = ('default', 'default', 'default', 1)

        self.timers_db = Timers_Database()
        self.parser = DataParser()
        self.users = self.parser.users()
        self.machines = self.parser.machines()
        #self.errors_journal.clicked.connect(self.open_errors_table)
        self.timers_journal.clicked.connect(self.open_timers_table)
        self.login_b.clicked.connect(self.open_login_widget)
        self.graph_b.clicked.connect(self.set_up_diagram)
        self.stat_b.clicked.connect(self.set_up_table)

        self.set_filters.clicked.connect(self.table_content)

        self.users_box = CheckableComboBox(self)
        self.users_box.addItems(self.users)
        self.users_box.setGeometry(870, 10, 161, 35)
        self.users_box.show()

        self.machines_box =  CheckableComboBox(self)
        self.machines_box.addItems(self.machines)
        self.machines_box.setGeometry(870, 70, 161, 35)
        self.machines_box.show()
        self.create_table()

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh_table)
        self.timer.start()

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

    def table_content(self) -> None:

         self.set_filters.clicked.connect(self.table_content)
         conditions = self.set_up_filters()
         result_data = self.parser.date_to_table(conditions[0], conditions[1], conditions[2],conditions[3])
         summary_time = result_data['PROGRAM']

         self.prog_rel.setText(str(round(result_data['PROGRAM']/summary_time, 2)*100))
         self.task_rel.setText(str(round(result_data['TASK']/summary_time, 2)*100))
         self.laser_rel.setText(str(round(result_data['LASER']/summary_time, 2)*100))
         self.pause_rel.setText(str(round(result_data['PAUSE']/summary_time, 2)*100))
         self.gas_rel.setText(str(round(result_data['GAS']/summary_time, 2)*100))

         self.prog_abs.setText(self.convert_sec_to_time(result_data['PROGRAM']))
         self.task_abs.setText(self.convert_sec_to_time(result_data['TASK']))
         self.laser_abs.setText(self.convert_sec_to_time(result_data['LASER']))
         self.pause_abs.setText(self.convert_sec_to_time(result_data['PAUSE']))
         self.gas_abs.setText(self.convert_sec_to_time(result_data['GAS']))

         series = QtChart.QPieSeries()

         [series.append (*piece) for piece in [

         ('Задание', round(result_data['TASK']/summary_time, 2)*100),
         ('Лазер', round(result_data['LASER']/summary_time, 2)*100),
         ('Газ', round(result_data['GAS']/summary_time, 2)*100),
         ('Паузы', round(result_data['PAUSE']/summary_time, 2)*100)
         ]]

         pie = PieChartConstructor(series)
         pie.add_slice(0)
         clearLayout(self.diagram_place)
         self.diagram_place.addWidget(pie)
         print('all_right')

    def set_up_table(self):

        self.stackedWidget.setCurrentIndex(0)
        self.table_content()
        print('11')

    def set_up_diagram(self):

        operation_set = ['PROGRAM', 'TASK', 'PAUSE', 'LASER', 'GAS']

        self.stackedWidget.setCurrentIndex(1)
        filter_graphs_box = CheckableComboBox(self)
        filter_graphs_box.addItems(operation_set)
        #self.stackedWidget.filter_graphs_box.setGeometry(1180, 110, 161, 35)
        #filter_graphs_box.setGeometry(100, 110, 161, 35)
        #self.stackedWidget.addWidget(filter_graphs_box)
        #filter_graphs_box.show()
        #self.set_filters.clicked.connect(self.graphs_content)
        self.graphs_content()
        print('22')

    def create_table(self):

        header_font = QFont('Sergoe UI', 12)
        header_font.setWeight(QFont.Bold)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels([ "Относительное время","Абсолютное время", "Название операции"])
        self.tableWidget.horizontalHeaderItem(0).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(1).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(2).setFont(header_font)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)

    def add_to_table(self, list):

        rowPos = self.tableWidget.rowCount()


    def refresh_table(self, i):

        rows = self.tableWidget.rowCount()
        for row in range(rows):
            _data = self.tableWidget.item(row, 3).text()
            time_abs = self.time_abs_func([_data,])
            self.tableWidget.setItem(row, 1, QTableWidgetItem(time_abs))

    def graphs_content(self):

        self.set_filters.clicked.connect(self.graphs_content)
        clearLayout(self.machines_layout)
        clearLayout(self.users_layout)
        clearLayout(self.graphs_layout)
        conditions = self.set_up_filters()
        operations = ['1', '2', '3']
        result_data = self.parser.date_to_table(conditions[0], conditions[1], conditions[2], conditions[3])
        self.stackedWidget.setCurrentIndex(1)

        machines = conditions[3]
        users = conditions[2]

        for machine in machines:

            lbl = QLabel()
            lbl.setText(machine)
            self.machines_layout.addWidget(lbl)

            for user in users:

                groupbox = QGroupBox()
                lbl = QLabel()
                lbl.setText(user)
                self.users_layout.addWidget(lbl)
                base_layout = QGridLayout()
                self.graphs_layout.addLayout(base_layout)

                _ = 0
                for operation in operations:
                    _ =_ + 1
                    layout = QHBoxLayout()
                    frame1 = QFrame()
                    frame2 = QFrame()
                    layout.addWidget(frame1)
                    layout.addWidget(frame2)
                    base_layout.addLayout(layout, _ , 2)


    def convert_sec_to_time(self, seconds) -> str:

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


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

    def open_filters(self):

        self.filters = FiltersWindow(self.users_db, self.machines_db)
        self.filters.show()

    def update_timer(self):

        self.setItem(0, 0, QtWidgets.QTableWidgetItem(str(my_timer)))



    def exp_to_xlsx():

        pass


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
