from PyQt5 import QtWidgets, uic, QtChart, QtCore, QtGui
from PyQt5.QtWidgets import  QComboBox, QApplication, QAction, QMainWindow, QGraphicsScene, QLabel, QFrame, QGroupBox, QHBoxLayout, QGridLayout, QCalendarWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,  QPushButton, QMenu
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QSize, Qt, QTimer, QObject, pyqtSignal, pyqtSlot, QThread
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
import socket
import codecs
from datetime import datetime
import threading
from widgets.login_widget import LoginWindow
from PyQt5 import QtCore
import ctypes
from ctypes import wintypes
from data_parser import DataParser
from widgets.combobox import CheckableComboBox
from collections import defaultdict

# Create the Slots that will receive signals


class DataRecieve(QThread):

    signal_Data = pyqtSignal(['QString'])

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def parsing_message(self, message):

        msg_to_pars = codecs.decode(message, 'UTF-8')
        msg_to_pars = msg_to_pars[1 : -1]
        msg_to_list = msg_to_pars.split(',')
        data = []
        for msg in msg_to_list:
            msg = msg.split(':"')
            msg = msg[-1][0:-1]
            data.append(msg)
        return msg_to_pars

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 12345       # Port to listen on (non-privileged ports are > 1023)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        while True:
            with s:
                request = conn.recv(1024)
                len_message = int.from_bytes(request[:2], 'big')
                msg_to_pars = request[2:len_message+1]
                data = self.parsing_message(msg_to_pars)
                self.signal_Data.emit(data)

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
        self.users = self.parser.users()
        self.machines = self.parser.machines()

        self.users_box = CheckableComboBox(self) #create combobox to choice users
        self.users_box.addItems(self.users) # add users list from DataParser to combobox
        self.users_box.show()

        self.machines_box =  CheckableComboBox(self) #create combobox to choice machines
        self.machines_box.addItems(self.machines) # add machines list from DataParser to combobox
        self.machines_box.show()

        self.users_lay.addWidget(self.users_box)
        self.set_filters.clicked.connect(self.filter_data)

        self.operation_list = []
        self.operations = defaultdict(list)
        #self.refresh_values()
        self.create_diagram()

        self.add_data_thread = DataRecieve()
        self.add_data_thread.signal_Data.connect(self.on_Data)
        self.add_data_thread.start()

        # table_append_thread = QtCore.QThread()
        # table_append_thread.started.connect(self.add_to_table)
        # table_append_thread.start()

        #self.timers_journal.clicked.connect(self.open_timers_table)
        #self.reset_filters.clicked.connect(self.reboot_timers)
        #self.tabWidget.stat.clicked.connect(set_up_table)
        #self.graph_b.clicked.connect(self.set_up_barcharts)
        #self._createActions()
        #self._createMenuBar()

    @pyqtSlot(str)
    def on_Data(self, message): #В теле функции обработка приходящих данных
        data = []
        msg_to_list = message.split(',')
        for msg in msg_to_list:
            msg = msg.split(':"')
            msg = msg[-1][0:-1]
            data.append(msg)

        date_now = datetime.now()
        event = data[2]
        dtime_event = data[0]
        status_event = data[3]
        rowPos = self.timers_table.rowCount() #count position to insert new row
        rowPos_err = self.timers_table.rowCount()
        if event not in self.operations.keys() and event!= 'ERROR':

            self.timers_table.insertRow(rowPos) # insert new row to the counted position
            self.timers_table.setItem(rowPos, 0, QTableWidgetItem(event))
            self.operations[event] = [status_event, dtime_event]

            datetime_event = datetime.strptime(dtime_event, '%Y-%m-%d %H:%M:%S')
            dtime_rel = (date_now - datetime_event).total_seconds() #count seconds for calculate relative operation time
            dtime_abs = self.convert_sec_to_time(dtime_rel) #convert seconds to format hours:minutes:seconds (HH:MM:SS)
            self.timers_table.setItem(rowPos, 1, QTableWidgetItem(dtime_event))
            _slice = QPieSlice(event,dtime_rel, self.series)
            # _slice.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]) )
            _slice.setLabelVisible(True)
            self.series.append(_slice)
            for slice in self.series.slices():
                slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            self.series.setLabelsPosition(QPieSlice.LabelInsideNormal)
            self.chart.legend().setVisible(True)
            self.chart.legend().setAlignment(Qt.AlignBottom)
            i = len(self.series)
            self.chart.legend().markers(self.series)[i-1].setLabel(event)

        elif event not in self.operations.keys():

            rowPos_err = self.errors_table.rowCount()
            self.errors_table.insertRow(rowPos_err) # insert new row to the counted position
            self.errors_table.setItem(rowPos_err, 0, QTableWidgetItem(status_event))
            datetime_event = datetime.strptime(dtime_event, '%Y-%m-%d %H:%M:%S')
            self.errors_table.setItem(rowPos_err, 1, QTableWidgetItem(dtime_event))


    @pyqtSlot(list)
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
        header_font = QFont('Sergoe UI', 11)
        header_font.setWeight(QFont.Bold)
        # create table template for append date from timers_database
        self.timers_table =  QTableWidget(self)
        self.timers_table.setColumnCount(3)
        self.timers_table.setHorizontalHeaderLabels(["Название", "Абсолютное время", "Относительное время"])
        header = self.timers_table.horizontalHeader()
        self.timers_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.timers_table.setSortingEnabled(True)
        for i in range(self.timers_table.columnCount()):

            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.timers_table.horizontalHeaderItem(0).setFont(header_font)
        self.timers_table.horizontalHeaderItem(1).setFont(header_font)
        self.timers_table.horizontalHeaderItem(2).setFont(header_font)
        self.timers_table.resizeRowsToContents()
        self.timers_table.resizeColumnsToContents()
        self.stat_up_layout.addWidget(self.timers_table)

        self.errors_table =  QTableWidget(self)
        self.errors_table.setColumnCount(2)
        self.errors_table.setHorizontalHeaderLabels(["Название ошибки", "Время возникновения"])
        header = self.errors_table.horizontalHeader()
        self.errors_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.errors_table.setSortingEnabled(True)
        for i in range(self.errors_table.columnCount()):

            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.errors_table.horizontalHeaderItem(0).setFont(header_font)
        self.errors_table.horizontalHeaderItem(1).setFont(header_font)
        self.errors_table.resizeRowsToContents()
        self.errors_table.resizeColumnsToContents()
        self.gridLayout_4.addWidget(self.errors_table)

    def create_donutchart(self):

        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append("Protein 4.2%", 4.2)
        slice = QPieSlice()
        slice = series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Other 23.8%", 23.8);
        series.append("Carbs 56.4%", 56.4);
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("DonutChart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartview)

    # def create_diagram(self):
    #
    #     #self.clearLayout(self.diagram_up)
    #     self.series = QtChart.QPieSeries()# create series for diagram
    #     self.series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal) #set horizontal label for diagram
    #
    #     self.series = QPieSeries()
    #     self.series.setHoleSize(0.35) # change relative size of central hole in diagram
    #     self.series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
    #     self.series.setLabelsVisible(True)
    #     self.slice = QPieSlice()
    #     self.slice.setExploded(True)
    #     self.slice.setLabelVisible(True)
    #
    #     chart = QChart()
    #     chart.legend().hide()
    #     chart.addSeries(series)
    #     chart.setAnimationOptions(QChart.SeriesAnimations)
    #     chart.setTitle("DonutChart Example")
    #     chart.setTheme(QChart.ChartThemeBlueCerulean)
    #     chartview = QChartView(chart)
    #     chartview.setRenderHint(QPainter.Antialiasing)
    #     for slice in self.series.slices():
    #         slice.setLabel("<h3>{:.2f}%</h3>".format(100 * slice.percentage()))
    #     self.chart = QChart()
    #     #self.chart.legend().hide()
    #     self.chart.addSeries(self.series)
    #     header_font = QFont('Sergoe UI', 12)
    #     self.chart.legend().setFont(header_font)
    #     self.chart.setAnimationOptions(QChart.SeriesAnimations)
    #     self.title = "<span style='color: black; font-size: 18pt;'>Статистика по операциям</span>"
    #     self.chart.setTitle(self.title)
    #     self.chartview = QChartView(self.chart)
    #     self.chartview.setRenderHint(QPainter.Antialiasing)
    #     # self.clearLayout(self.diagram_up)
    #     self.clearLayout(self.gridLayout)
    #     self.diagram_up.addWidget(self.chartview)

    def create_diagram(self):

        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        self.slice = QPieSlice()
        self.slice.setExploded()
        self.slice.setLabelVisible()
        for slice in self.series.slices():
            slice.setLabel("<h3>{:.2f}%</h3>".format(100 * slice.percentage()))
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("<span style='color: black; font-size: 18pt;'>Статистика по операциям</span>")
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.diagram_up.addWidget(self.chartview)

    def refresh_table(self):
        dict = self.parser.operations_d
        print(dict)
        rows = self.timers_table.rowCount()
        date_now = datetime.now()
        summary_time = 0
        for row in range(0, rows):
           operation_name = self.timers_table.item(row, 0).text()
           if operation_name!='ERROR_1' :
               if dict[operation_name][-1][-1]  == 'START\\n':
                   datetime_event = datetime.strptime(dict[operation_name][0][0], '%Y-%m-%d %H:%M:%S')
                   dtime_rel = (date_now - datetime_event).total_seconds()
                   dtime_abs = self.convert_sec_to_time(dtime_rel)
                   self.timers_table.setItem(row, 1, QTableWidgetItem(str(dtime_abs)))
                   summary_time = summary_time + dtime_rel
                   self.timers_table.setItem(row, 2, QTableWidgetItem(str(round(dtime_rel/summary_time*100,2))))
               else:
                   datetime_event = datetime.strptime(dict[operation_name][0][0], '%Y-%m-%d %H:%M:%S')
                   dtime_rel = (date_now - datetime_event).total_seconds()
                   summary_time = summary_time + dtime_rel
                   self.timers_table.setItem(row, 2, QTableWidgetItem(str(round(dtime_rel/summary_time*100,2))))
                   print(135)

    def add_data(self):
        self.series.append("Other 23.8%", 23.8)
        self.series.append("Carbs 56.4%", 56.4)

    @pyqtSlot(list)
    def add_to_table(self, data) -> None:

        '''
        Add new data to operations table and operations diagram
        '''
        dict = self.parser.operations_d
        date_now = datetime.now()
        event = data[0]
        rowPos = self.timers_table.rowCount() #count position to insert new row
        print(self.operation_list)
        if data[0] not in self.operation_list and data[0]!= None:
            self.operation_list.append(data[0])
            self.timers_table.insertRow(rowPos) # insert new row to the counted position
            self.timers_table.setItem(rowPos, 0, QTableWidgetItem(data[0]))
            datetime_event = datetime.strptime(dict[event][-1][-2], '%Y-%m-%d %H:%M:%S')
            dtime_rel = (date_now - datetime_event).total_seconds() #count seconds for calculate relative operation time
            dtime_abs = self.convert_sec_to_time(dtime_rel) #convert seconds to format hours:minutes:seconds (HH:MM:SS)
            self.timers_table.setItem(rowPos, 1, QTableWidgetItem(dtime_abs))
            self.series.remove(self.series.slices()[0])

            _slice = QPieSlice(f'New data {self.num_data}', random.randint(5, 30), self.series)
            _slice.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]) )
            _slice.setLabelVisible(True)
            self.series.append(_slice)

            for slice in self.series.slices():
                slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            self.series.setLabelsPosition(QPieSlice.LabelInsideNormal)
            self.chart.legend().markers(self.series)[4].setLabel(f'New_data: {self.num_data}')

            self.num_data += 1

    def convert_sec_to_time(self, seconds) -> str:

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        # operations = list(dict.keys())
        # date_now = datetime.now() # give current datetime from calling python build-in method .now()
        #
        # self.list = [] #list of operations wich is currently in the table
        #
        # # print(self.parser.msg_status)
        # # self.parser.msg_status =  0
        # for operation in operations: # iterate in operations list
        #
        #     if operation not in self.list: # if operation not in list of operations - append new string in table with new operations
        #
        #         rowPos = self.tableWidget.rowCount() #count position to insert new row
        #         self.tableWidget.insertRow(rowPos) # insert new row to the counted position
        #         datetime_event = datetime.strptime(dict[operation][-1][-2], '%Y-%m-%d %H:%M:%S')
        #         dtime_rel = (date_now - datetime_event).total_seconds() #count seconds for calculate relative operation time
        #         dtime_abs = self.convert_sec_to_time(dtime_rel) #convert seconds to format hours:minutes:seconds (HH:MM:SS)
        #         self.summary_time = self.summary_time + dtime_rel # add relative time to total time of overall operations
        #
        #         self.tableWidget.setItem(rowPos, 1, QTableWidgetItem(dtime_abs)) #set new items in the table
        #         self.tableWidget.setItem(rowPos, 0, QTableWidgetItem(str(dtime_rel/self.summary_time)))
        #         self.tableWidget.setItem(rowPos, 2, QTableWidgetItem(operation))
        #
        #         self.list.append(operation) #append new operation in the operations list
        #         self.series.append(operation, dtime_rel/self.summary_time) #
        #self.diagram_up.addWidget(self.chartview)

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
        pass

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

    def clearLayout(self, layout):

      while layout.count():

        child = layout.takeAt(0)

        if child.widget():

          child.widget().deleteLater()

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
