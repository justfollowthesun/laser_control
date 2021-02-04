import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

class BarChart(QtWidgets.QMainWindow):

	def __init__(self):

		super().__init__()
		
		self.resize(800, 600)

		set0 = QBarSet('Выполнение программы')
		set1 = QBarSet('Выполнение задания')
		set2 = QBarSet('Работа лазера')
		set3 = QBarSet('Паузы')
		set4 = QBarSet('Газ')

		set0.append([1, 2])
		set1.append([5, 0, 0, 4, 0, 7])
		set2.append([3, 5, 8, 13, 8, 5])
		set3.append([5, 6, 7, 3, 4, 5])
		set4.append([9, 7, 5, 3, 1, 2])

		series = QHorizontalBarSeries()
		series.append(set0)
		series.append(set1)
		series.append(set2)
		series.append(set3)
		series.append(set4)

		chart = QChart()
		chart.addSeries(series)
		chart.setTitle('Horizontal Bar Chart Demo')

		chart.setAnimationOptions(QChart.SeriesAnimations)

		months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June')

		axisY = QBarCategoryAxis()
		axisY.append(months)
		chart.addAxis(axisY, Qt.AlignLeft)
		series.attachAxis(axisY)

		axisX = QValueAxis()
		chart.addAxis(axisX, Qt.AlignBottom)
		series.attachAxis(axisX)

		axisX.applyNiceNumbers()

		chart.legend().setVisible(True)
		chart.legend().setAlignment(Qt.AlignBottom)

		chartView = QChartView(chart)
		chartView.setRenderHint(QPainter.Antialiasing)
		self.setCentralWidget(chartView)

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())
