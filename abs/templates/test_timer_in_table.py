import sys

from PyQt5 import QtWidgets, QtCore
from time import time


class TimerInTableExample(QtWidgets.QMainWindow):

    default = 5
    t = default

    def __init__(self):
        super().__init__()
        self.initUI()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_time)

        # update the timer every second
        timer.start(1000)

    def update_time(self):

        if self.t != 0:
            mins, secs = divmod(self.t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.t -= 1
        else:
            self.t = self.default
            timer = '00:00'

        self.table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem(timer))

    def initUI(self):
        self.setMinimumSize(100, 100)
        self.setWindowTitle("Timer in a table example")
        self.createTable()
        self.show()

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TimerInTableExample()
    sys.exit(app.exec_())
