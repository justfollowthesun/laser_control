import sys
import random
from typing import List, Optional, Union

from PyQt5 import QtChart, QtGui, QtWidgets, QtCore

class PieChartConstructor(QtChart.QChartView):

    def __init__(self, series: List[QtChart.QPieSeries], title: Optional[str] = None) -> None:

        self.series = series
        print(series.slices())

        self.title = "Статистика по операциям"

        chart = QtChart.QChart()
        chart.addSeries(self.series)

        # chart.legend().hide()
        # chart.createDefaultAxes()

        chart.setTitle(self.title)

        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        # chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        super().__init__(chart)
        self.setRenderHint(QtGui.QPainter.Antialiasing)

    def add_slice(self, slice: Union[int, QtChart.QPieSlice], change_color: bool = True) -> None:
        if isinstance(slice, int):
            slice: QtChart.QPieSlice = self.series.slices()[slice]

        slice.setExploded(True)
        slice.setLabelVisible(True)

        if change_color:

            # цвет и толщина контура
            slice.setPen(QtGui.QPen(QtCore.Qt.black, 1))
            slice.setBrush(QtCore.Qt.green)

    def update_series(self, slice: QtChart.QPieSlice) -> None:

        slice.setValue(slice.value() + random.randint(-2, 2))

    def slice_clicked(self, slice: QtChart.QPieSlice) -> None:

        exploded = slice.isExploded()

        for s in self.series.slices():
            if s.isExploded():
                s.setExploded(False)
                s.setLabelVisible(False)

        if not exploded:
            self.add_slice(slice, change_color=False)


class PieChartExample(QtWidgets.QMainWindow):

    def __init__(self) -> None:

        super().__init__()
        self.setWindowTitle("Время выполнения операций")
        self.setMinimumSize(700, 500)
        chartview = self.create_piechart()
        self.setCentralWidget(chartview)
        chartview.series.hovered.connect(chartview.update_series)
        chartview.series.clicked.connect(chartview.slice_clicked)

    def bla(self):
        self.setStyleSheet(f"background-color: {random.choice(['lightgrey', '#432', 'white', 'grey'])};")

    def create_piechart(self) -> QtChart.QChartView:

        series = QtChart.QPieSeries()
        [series.append(*piece) for piece in data]
        pie = PieChartConstructor(series)
        pie.add_slice(0)
        return pie


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PieChartExample()
    window.show()
    app.exec_()
