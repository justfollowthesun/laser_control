from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QPushButton,  QLabel, QFrame, QGroupBox, QHBoxLayout, QGridLayout, QCalendarWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import *
from datetime import datetime
from config import UI_LOGIN_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget
from config import UI_TIMERS_WINDOW
from datetime import datetime
from config import DB_TIMERS_PATH, DB_DIR
from storage.timers_database import Timers_Database

Ui_TimersWindow, _ = uic.loadUiType(UI_TIMERS_WINDOW, import_from = DESIGN_DIR)

class TimersWindow(QtWidgets.QWidget, Ui_TimersWindow):

    connection = None

    def __init__(self, database: Timers_Database) -> None:

        QtWidgets.QWidget.__init__(self)
        Ui_TimersWindow.__init__(self)
        self.setupUi(self)
        self.timers_db = Timers_Database()
        self.set_up_timers()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh_timers)
        self.timer.start()
        #self.operation_1_reset.clicked.connect(self.reset_timers)

    def set_up_timers(self):

        header_font = QFont('Sergoe UI', 12)
        header_font.setWeight(QFont.Bold)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels([ "Название", "Время до замены (ДД:ЧЧ: ММ)","Комментарий", "Пояснения для решения проблемы", "Сброс таймера" ])
        self.tableWidget.horizontalHeaderItem(0).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(1).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(2).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(3).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(4).setFont(header_font)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 450)
        self.tableWidget.setColumnWidth(3, 450)
        self.tableWidget.setColumnWidth(4, 250)
        list_to_add = self.timers_db.select_data()


        buttons =[QPushButton(self.tableWidget) for i in range(len(list_to_add))]

        for timer, button in zip(list_to_add, buttons):

            rowPos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPos)
            self.tableWidget.setItem(rowPos, 0, QTableWidgetItem(timer[0]))
            print(timer)
            datetime_obj = datetime.strptime(timer[2], '%Y/%m/%d/%H/%M/%S')
            time_delta = (datetime_obj - datetime.now()).total_seconds()
            new_value = self.convert_sec_to_time(time_delta)

            self.tableWidget.setItem(rowPos, 1, QTableWidgetItem(new_value))
            self.tableWidget.setItem(rowPos, 2, QTableWidgetItem(timer[4]))
            self.tableWidget.setItem(rowPos, 3, QTableWidgetItem(timer[5]))
            button.setStyleSheet(
                "QPushButton"
                "{"
	             "background-color: white ;"
	             "border-radius:5px;"
	             "color: black;"
	             "border: 2px solid rgb(247, 247, 247);"
	             "border-color: green"
                 "}"

                 "QPushButton:hover"
                 "{"
	              "border: 2px solid rgb(247, 247, 247);"
	              "border-color: orange;"
                  "}"

                  "QPushButton:pressed"
                  "{"
	              "background-color: rgb(88, 88, 88);"
                  "}"
                  )
            button.setText('Сбросить')
            button.clicked.connect(
        lambda ch, t=timer[6], r=rowPos:  self.reset_timers(t, r)
    )
            #button.clicked.connect(lambda: self.reset_timers(timer[6], rowPos))
            self.tableWidget.setCellWidget(rowPos, 4, button)
            self.tableWidget.resizeColumnsToContents()

        #list_to_add = self.parser.parsing() #[operation date, operation name, status]

    def refresh_timers(self):

        _ = 0
        for timer in self.list_to_add:

            datetime_obj = datetime.strptime(timer[2], '%Y/%m/%d/%H/%M/%S')
            time_delta = (datetime_obj - datetime.now()).total_seconds()
            new_value = self.convert_sec_to_time(time_delta)
            print(new_value)
            self.tableWidget.setItem(_, 1, QTableWidgetItem(new_value))
            _ = _ + 1

    def convert_sec_to_time(self, seconds) -> str:

        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return '{:02}:{:02}:{:02}'.format(int(days), int(hours), int(minutes))

    def reset_timers(self, timer_id, rowPos):

        print(timer_id, rowPos)
        self.timers_db.reset_timer_data(timer_id)
        self.list_to_add = self.timers_db.select_data()
        self.refresh_timers()
        #self.operation_1.setText(self.timers_db.reset_timer_data(timer_id))
        #self.operation_1.setText(self.timers_db.select_data(timer_id))


    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()
