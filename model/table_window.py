import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


def timerEvent(table_class):


    table_class._data = table_class.time.toString("hh:mm:ss")


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super(TableModel, self).__init__()
        self.create_timers()

    def create_timers(self):

        self._data = []
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        # self.timer.timeout.connect(lambda: timerEvent(self))
        self.timer.timeout.connect(self.change_data_value)
        self.timer.setInterval(1000)
        self.timer.start()

    def change_data_value(self):

        self.time = self.time.addSecs(1)
        self._data = self.time.toString("hh:mm:ss")
        # self._data = self.timer.remainingTime()


    def data(self, index, role):

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data # self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return 1 # len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 1 # len(self._data[0])
