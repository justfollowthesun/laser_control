import sys
import random
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Qt5Agg')

from pprint import pprint
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class PieChartExample(FigureCanvasQTAgg):

    def __init__(self) -> None:

        self.figure, self.axis = plt.subplots()

        x = random.randint(20, 50)
        y = 100 - x
        self.axis.pie([x,y], explode=[0,0], labels=['x', 'y'], autopct='%1.1f%%', shadow=True, startangle=90)

        # self.axis.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

        # Equal aspect ratio ensures that pie is drawn as a circle.
        # self.axis.axis('equal')

        super().__init__(self.figure)


class MainWindow(QtWidgets.QMainWindow):

    x = random.randint(0, 90)
    direction = 1

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.new_pie = PieChartExample()
        self.setCentralWidget(self.new_pie)

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.new_pie.axis.clear()
        self.x += 5 * self.direction

        if self.x > 100:
            self.x = 95
            self.direction = -1
        elif self.x < 0:
            self.x = 5
            self.direction = 1

        y = 100 - self.x
        self.new_pie.axis.pie([self.x ,y], explode=[0,0], labels=['x', 'y'], autopct='%1.1f%%', shadow=True, startangle=90)
        self.new_pie.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
