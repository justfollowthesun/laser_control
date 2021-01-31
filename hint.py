import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

class MainWindow(QMainWindow):

	def __init__(self):

		super().__init__()
		self.resize(800, 600)

		set0 = QBarSet('X0')
		set1 = QBarSet('X1')
		set2 = QBarSet('X2')
		set3 = QBarSet('X3')
		set4 = QBarSet('X4')

		set0.append([1, 2, 3, 4, 5, 6])
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


# import plotly.offline as po
# import plotly.graph_objs as go
# from PyQt5 import QtWebEngineWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5 import QtCore, QtWidgets
# import sys
#
#
# def show_qt(fig):
#     raw_html = '<html><head><meta charset="utf-8" />'
#     raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
#     raw_html += '<body>'
#     raw_html += po.plot(fig, include_plotlyjs=False, output_type='div')
#     raw_html += '</body></html>'
#
#     fig_view = QWebEngineView()
#     # setHtml has a 2MB size limit, need to switch to setUrl on tmp file
#     # for large figures.
#     fig_view.setHtml(raw_html)
#     fig_view.show()
#     fig_view.raise_()
#     return fig_view
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#
#     fig = go.Figure(data=[{'type': 'scattergl', 'y': [2, 1, 3, 1]}])
#     fig_view = show_qt(fig)
#     sys.exit(app.exec_())
