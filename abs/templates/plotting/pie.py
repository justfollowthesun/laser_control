import sys
import matplotlib

try:
    matplotlib.use('Qt5Agg')
finally:
    from PyQt5 import QtWidgets

    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
    import matplotlib.pyplot as plt


class PieChartExample(FigureCanvasQTAgg):

    def __init__(self) -> None:

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]

        # only "explode" the 2nd slice (i.e. 'Hogs')
        explode = (0, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180)

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')

        super().__init__(fig1)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        new_pie = PieChartExample()

        self.setCentralWidget(new_pie)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
