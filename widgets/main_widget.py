from PyQt5 import QtWidgets, uic, QtChart, QtCore, QtGui
from PyQt5.QtWidgets import  QComboBox, QApplication, QAction, QMainWindow, QGraphicsScene, QLabel, QFrame, QGroupBox, QHBoxLayout, QGridLayout, QCalendarWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,  QPushButton, QMenu
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtChart import QChart
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from datetime import datetime
from config import UI_MAIN_WINDOW, UI_LOGIN_WINDOW, DESIGN_DIR
from PyQt5.QtGui import QIcon
from abs.qt import MoveableWidget
import time
import sys
from datetime import datetime
import threading
from widgets.login_widget import LoginWindow
from PyQt5 import QtCore
import ctypes
from ctypes import wintypes
from data_parser import DataParser
from widgets.combobox import CheckableComboBox


Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from = DESIGN_DIR)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MoveableWidget):

    my_timer = 0

    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.user = ('default', 'default', 'default', 1) #create default user array
        self.parser = DataParser() # connect to data parser
        #self.login_b.clicked.connect(self.open_login_widget)
        #self.stat_b.clicked.connect(self.set_up_table)
        self.create_table()
        self.add_to_table()
        self.users = self.parser.users()
        self.machines = self.parser.machines()

        self.users_box = CheckableComboBox(self) #create combobox to choice users
        self.users_box.addItems(self.users) # add users list from DataParser to combobox
        self.users_box.show()

        self.machines_box =  CheckableComboBox(self) #create combobox to choice machines
        self.machines_box.addItems(self.machines) # add machines list from DataParser to combobox
        self.machines_box.show()

        self.users_lay.addWidget(self.users_box)
        self.equipments_lay.addWidget(self.machines_box)

        self.set_filters.clicked.connect(self.filter_data)

        ip_connect_thread = threading.Thread(target = self.give_data)
        ip_connect_thread.start()

        add_data = threading.Thread(target = self.add_table)
        add_data.start()

        self.refresh_values()

        # table_refresh_thread = QtCore.QThread()
        # table_refresh_thread.started.connect(self.refresh_values)
        # table_refresh_thread.start()

        # table_append_thread = QtCore.QThread()
        # table_append_thread.started.connect(self.add_to_table)
        # table_append_thread.start()

        #self.timers_journal.clicked.connect(self.open_timers_table)
        #self.reset_filters.clicked.connect(self.reboot_timers)
        #self.tabWidget.stat.clicked.connect(set_up_table)
        print('all right')
        #self.graph_b.clicked.connect(self.set_up_barcharts)
        #self._createActions()
        #self._createMenuBar()

    def give_data(self):

        self.parser.ip_connect()

    def add_table(self):
        while True:
             if self.parser.data_signal == 1:
                 print(self.parser.data)
                 self.parser.data_signal = 0


    def refresh_values(self):

        self.parser_timer = QTimer(self) # create timer to dynamycally update operations table
        self.parser_timer.setInterval(1000) # set time values to refresh timer (1000 equivalent to 1 sec)
        self.parser_timer.start()
        self.parser_timer.timeout.connect(self.refresh_table)

    def set_up_filters(self) -> list:

        '''
        Return filter values, which initialized by user in MainWindow
        '''

        start_date = self.start_date.date().toPyDate() #convert values from calendar widget to python date and python time
        start_time = self.start_time.time().toPyTime()
        start_datetime = datetime.combine(start_date, start_time)
        start_datetime_to_str = datetime.strftime(start_datetime, '%Y-%m-%d %H:%M:%S') #convert python date and time to string


        finish_date = self.finish_date.date().toPyDate()
        finish_time = self.finish_time.time().toPyTime()
        finish_datetime = datetime.combine(finish_date, finish_time)
        finish_datetime_to_str = datetime.strftime(finish_datetime, '%Y-%m-%d %H:%M:%S')

        users = self.users_box.currentData() # list of users from users combobox
        equipment = self.machines_box.currentData() # list of machines from machines combobox

        #merge start datetime, finish datetime, users, machines to list
        return start_datetime_to_str, finish_datetime_to_str, users, equipment # return list [start datetime: string, finish datetime: string, users: list, equipment: list]

    #def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&amp;New")
        # Creating actions using the second constructor
        self.openAction = QAction("&amp;Open...", self)
        self.saveAction = QAction("&amp;Save", self)
        self.exitAction = QAction("&amp;Exit", self)
        self.copyAction = QAction("&amp;Copy", self)
        self.pasteAction = QAction("&amp;Paste", self)
        self.cutAction = QAction("C&amp;ut", self)
        self.helpContentAction = QAction("&amp;Help Content", self)
        self.aboutAction = QAction("&amp;About", self)

    #def _createMenuBar(self):

        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("&amp;File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        # Edit menu
        editMenu = menuBar.addMenu("&amp;Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        # Help menu
        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&amp;Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def set_up_barcharts(self) -> None:

        filter_graphs_box = CheckableComboBox(self)
        filter_graphs_box.addItems(operation_set)
        self.bar_charts_content()

    def create_table(self) -> None:
        '''
        Create empty table templatre with initial parameters
        Create diagram template
        '''
        header_font = QFont('Sergoe UI', 12) #set up header font
        header_font.setWeight(QFont.Bold) #set up header font weight
        self.tableWidget.setColumnCount(3) # create table template
        self.tableWidget.setHorizontalHeaderLabels([ "Относительное время","Абсолютное время", "Название операции"])
        self.tableWidget.horizontalHeaderItem(0).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(1).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(2).setFont(header_font)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)

    def create_diagram(self):

        self.diagram_series = QtChart.QPieSeries()# create series for diagram
        self.diagram_series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal) #set horizontal label for diagram

        self.series = QPieSeries()
        self.series.setHoleSize(0.35) # change relative size of central hole in diagram
        self.series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        self.slice = QPieSlice()
        self.slice.setExploded(True)
        self.slice.setLabelVisible(True)
        for slice in self.series.slices():
            slice.setLabel("<h3>{:.2f}%</h3>".format(100 * slice.percentage()))
        self.chart = QChart()
        #self.chart.legend().hide()
        self.chart.addSeries(self.series)
        header_font = QFont('Sergoe UI', 12)
        self.chart.legend().setFont(header_font)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.title = "<span style='color: black; font-size: 18pt;'>Статистика по операциям</span>"
        self.chart.setTitle(self.title)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.clearLayout(self.diagram_up)
        self.tableWidget.setRowCount(0)
        self.clearLayout(self.gridLayout)

    def add_to_table(self) -> None:

        '''
        Add new data to operations table and operations diagram

        '''
        dict = self.parser.operations_d
        operations = list(dict.keys())
        date_now = datetime.now() # give current datetime from calling python build-in method .now()

        self.list = [] #list of operations wich is currently in the table

        # print(self.parser.msg_status)
        # self.parser.msg_status =  0
        for operation in operations: # iterate in operations list

            if operation not in self.list: # if operation not in list of operations - append new string in table with new operations

                rowPos = self.tableWidget.rowCount() #count position to insert new row
                self.tableWidget.insertRow(rowPos) # insert new row to the counted position
                datetime_event = datetime.strptime(dict[operation][-1][-2], '%Y-%m-%d %H:%M:%S')
                dtime_rel = (date_now - datetime_event).total_seconds() #count seconds for calculate relative operation time
                dtime_abs = self.convert_sec_to_time(dtime_rel) #convert seconds to format hours:minutes:seconds (HH:MM:SS)
                self.summary_time = self.summary_time + dtime_rel # add relative time to total time of overall operations

                self.tableWidget.setItem(rowPos, 1, QTableWidgetItem(dtime_abs)) #set new items in the table
                self.tableWidget.setItem(rowPos, 0, QTableWidgetItem(str(dtime_rel/self.summary_time)))
                self.tableWidget.setItem(rowPos, 2, QTableWidgetItem(operation))

                self.list.append(operation) #append new operation in the operations list
                self.series.append(operation, dtime_rel/self.summary_time) #
        #self.diagram_up.addWidget(self.chartview)

    def refresh_table(self):

        dict = self.parser.operations_d
        date_now = datetime.now()
        rows = self.tableWidget.rowCount()

        for row in range(rows):

            operation_name = self.tableWidget.item(row, 2).text()
            if dict[operation_name][-1][-1]  == 'START':

                datetime_event = datetime.strptime(dict[operation_name][-1][-2], '%Y-%m-%d %H:%M:%S')
                dtime_rel = (date_now - datetime_event).total_seconds()
                dtime_abs = self.convert_sec_to_time(dtime_rel)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(dtime_rel/self.summary_time)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(dtime_abs)))
                self.summary_time = self.summary_time + dtime_rel

        # if self.parser.msg_status == 1:
        #     self.add_to_table()
        #     self.parser.msg_status = 0

    def filter_data(self):

        start_dtime = self.start_dtime.dateTime().toPyDateTime()
        start_dtime_str = datetime.strftime(start_dtime, '%Y-%m-%d %H:%M:%S')

        finish_dtime = self.finish_dtime.dateTime().toPyDateTime()
        finish_str = datetime.strftime(finish_dtime, '%Y-%m-%d %H:%M:%S')

        users = self.users_box.currentData()
        equipment = self.machines_box.currentData()
        result_data = self.parser.data_from_filters(start_dtime, finish_dtime, users, equipment)
        total_sec = sum(result_data.values())
        self.tableWidget.setRowCount(0)

        for operation in result_data.keys():

                rowPos = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPos)

                dtime_rel = result_data[operation]
                dtime_abs = self.convert_sec_to_time(dtime_rel)

                self.tableWidget.setItem(rowPos, 1, QTableWidgetItem(dtime_abs))
                time_rel = round(dtime_rel/total_sec*100, 0)
                self.tableWidget.setItem(rowPos, 0, QTableWidgetItem(str(time_rel)))
                self.tableWidget.setItem(rowPos, 2, QTableWidgetItem(operation))

    def bar_charts_content(self) -> None:

        self.set_filters.clicked.connect(self.graphs_content) # NEED TO RESTRUCTURE, CONNECT WITH BOTH TABLE AND DIAGRAM
        clearLayout(self.machines_barcharts)
        clearLayout(self.users_barcharts)
        result = self.set_up_filters()

        users = result[3]
        machines = result[4]

        BarSetsUsers = {}
        BarSetsMachines = {}

        for user in users:

            BarSets[user] = QBarSet(user)
            BarSets[user].append([])

        for machine in machines:

            BarSetsMachines[machine] = QBarSet(machine)
            BarSetsMachines[machine].append([])
        print(BarSetsUsers, BarSetsMachines)

        for user in users:

            hours = self.parser.hours_from_user(user)

        # set0 = QBarSet('X0')
		# set1 = QBarSet('X1')
		# set2 = QBarSet('X2')
		# set3 = QBarSet('X3')
		# set4 = QBarSet('X4')
        #
		# set0.append([random.randint(0, 10) for i in range(6)])
		# set1.append([random.randint(0, 10) for i in range(6)])
		# set2.append([random.randint(0, 10) for i in range(6)])
		# set3.append([random.randint(0, 10) for i in range(6)])
		# set4.append([random.randint(0, 10) for i in range(6)])
        #
		# series = QBarSeries()
		# series.append(set0)
		# series.append(set1)
		# series.append(set2)
		# series.append(set3)
		# series.append(set4)
        #
		# chart = QChart()
		# chart.addSeries(series)
		# chart.setTitle('Bar Chart Demo')
		# chart.setAnimationOptions(QChart.SeriesAnimations)
        #
		# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')
        #
		# axisX = QBarCategoryAxis()
		# axisX.append(months)
        #
		# axisY = QValueAxis()
		# axisY.setRange(0, 15)
        #
		# chart.addAxis(axisX, Qt.AlignBottom)
		# chart.addAxis(axisY, Qt.AlignLeft)
        #
		# chart.legend().setVisible(True)
		# chart.legend().setAlignment(Qt.AlignBottom)
        #
		# chartView = QChartView(chart)
		# self.setCentralWidget(chartView)

        # clearLayout(self.graphs_layout)
        # conditions = self.set_up_filters()
        # operations = ['1', '2', '3']
        # result_data = self.parser.date_to_table(conditions[0], conditions[1], conditions[2], conditions[3])
        # self.stackedWidget.setCurrentIndex(1)
        #
        # machines = conditions[3]
        # users = conditions[2]
        #
        # for machine in machines:
        #
        #     lbl = QLabel()
        #     lbl.setText(machine)
        #     self.machines_layout.addWidget(lbl)
        #
        #     for user in users:
        #
        #         groupbox = QGroupBox()
        #         lbl = QLabel()
        #         lbl.setText(user)
        #         self.users_layout.addWidget(lbl)
        #         base_layout = QGridLayout()
        #         self.graphs_layout.addLayout(base_layout)
        #
        #         _ = 0
        #         for operation in operations:
        #             _ =_ + 1
        #             layout = QHBoxLayout()
        #             frame1 = QFrame()
        #             frame2 = QFrame()
        #             layout.addWidget(frame1)
        #             layout.addWidget(frame2)
        #             base_layout.addLayout(layout, _ , 2)

    def convert_sec_to_time(self, seconds) -> str:

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    def clearLayout(self, layout):

      while layout.count():

        child = layout.takeAt(0)

        if child.widget():

          child.widget().deleteLater()

    def open_login_widget(self):

        self.login_widget = LoginWindow(self.users_db, self)
        self.login_widget.show()
        self.login_widget.submit_button.clicked.connect(self.click_check)

    def open_timers_table(self):

        self.timers_table = TimersWindow(self.timers_db)
        self.timers_table.user = self.user
        print(self.user)
        self.timers_table.show()

    def click_check(self):

        self.user = self.login_widget.user

    def exp_to_xlsx():

        pass

    def convert_sec_to_time_timers(self, seconds) -> str:

        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}:{:02}'.format(int(days), int(hours), int(minutes))

    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()

def dump_data(main_window):

    data_save = []

    # rowCount() This property holds the number of rows in the table
    # for row in range(main_window.table.rowCount()):
    #     row_data = []
    #     for column in range(main_window.table.columnCount()):
    #     # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
    #         item = main_window.table.item(row, column).text()
    #         row_data.append(item)
    #         #item = main_window.table.item(row, column).text()
    #     print(f'row: {row}, column: {column}, row_data={row_data}')
    #     data_save.append(row_data)
    # print(data_save)

    with open('program_data.pkl', 'wb') as f:
        pickle.dump(data_save, f)
