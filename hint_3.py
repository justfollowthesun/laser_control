from PyQt5 import QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100, 100, 1280, 600)

        self.show()
        self.create_piechart()

    def create_piechart(self):
        series = QtChart.QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)
        series.setLabelsVisible(True)


        series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
        for slice in series.slices():
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        header_font = QFont('Sergoe UI', 12)


        chart.legend().markers(series)[0].setLabel("Python")
        chart.legend().markers(series)[1].setLabel("C++")
        chart.legend().markers(series)[2].setLabel("Java")
        chart.legend().markers(series)[3].setLabel("C#")
        chart.legend().markers(series)[4].setLabel("PHP")
        chart.legend().setFont(header_font)
        chartview = QChartView(chart)

        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
