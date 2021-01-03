import random
from PyQt5 import QtCore, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.table = QtWidgets.QTableWidget(5, 2, self)
        self.button = QtWidgets.QPushButton('Populate', self)
        self.button.clicked.connect(self.populate)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0)
        layout.addWidget(self.button, 1, 0)
        layout.setColumnStretch(1, 1)
        self.setCentalWidget(self.table)

    def populate(self):
        words = 'Red Green Blue Yellow Black White Purple'.split()
        length = random.randint(2, len(words))
        self.table.setRowCount(random.randint(3, 30))
        for column in range(self.table.columnCount()):
            for row in range(self.table.rowCount()):
                item = QtWidgets.QTableWidgetItem(' '.join(
                    random.sample(words, random.randint(1, length))))
                self.table.setItem(row, column, item)

        self.table.setVisible(False)
        self.table.verticalScrollBar().setValue(0)
        self.table.resizeColumnsToContents()
        self.table.setVisible(True)
        self.setTableWidth()

    def setTableWidth(self):
        width = self.table.verticalHeader().width()
        width += self.table.horizontalHeader().length()
        if self.table.verticalScrollBar().isVisible():
            width += self.table.verticalScrollBar().width()
        width += self.table.frameWidth() * 2
        self.table.setFixedWidth(width)

    def resizeEvent(self, event):
        self.setTableWidth()
        super(Window, self).resizeEvent(event)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(700, 150, 800, 400)
    window.show()
    sys.exit(app.exec_())
