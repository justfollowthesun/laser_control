from PyQt5 import QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


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

        chart.legend().markers(series)[0].setLabel("Python")
        chart.legend().markers(series)[1].setLabel("C++")
        chart.legend().markers(series)[2].setLabel("Java")
        chart.legend().markers(series)[3].setLabel("C#")
        chart.legend().markers(series)[4].setLabel("PHP")

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())



def bar_charts_content(self) -> None:

    set0 = QBarSet('X0')
    set1 = QBarSet('X1')
    set2 = QBarSet('X2')
    set3 = QBarSet('X3')
    set4 = QBarSet('X4')
    set0.append([random.randint(0, 10) for i in range(6)])
    set1.append([random.randint(0, 10) for i in range(6)])
    set2.append([random.randint(0, 10) for i in range(6)])
    set3.append([random.randint(0, 10) for i in range(6)])
    set4.append([random.randint(0, 10) for i in range(6)])
    series = QBarSeries()
    series.append(set0)
    series.append(set1)
    series.append(set2)
    series.append(set3)
    series.append(set4)
    chart = QChart()
    chart.addSeries(series)
    chart.setTitle('Bar Chart Demo')
    chart.setAnimationOptions(QChart.SeriesAnimations)
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')
    axisX = QBarCategoryAxis()
    axisX.append(months)
    axisY = QValueAxis()
    axisY.setRange(0, 15)
    chart.addAxis(axisX, Qt.AlignBottom)
    chart.addAxis(axisY, Qt.AlignLeft)
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)
    chartView = QChartView(chart)
    self.setCentralWidget(chartView)
    clearLayout(self.graphs_layout)
    conditions = self.set_up_filters()
    operations = ['1', '2', '3']
    result_data = self.parser.date_to_table(conditions[0], conditions[1], conditions[2], conditions[3])
    self.stackedWidget.setCurrentIndex(1)
    machines = conditions[3]
    users = conditions[2]

    self.set_filters.clicked.connect(self.graphs_content) # NEED TO RESTRUCTURE, CONNECT WITH BOTH TABLE AND DIAGRAM
    clearLayout(self.machines_barcharts)
    clearLayout(self.users_barcharts)
    result = self.set_up_filters()
    for machine in machines:

        lbl = QLabel()
        lbl.setText(machine)
        self.machines_layout.addWidget(lbl)

        for user in users:

            groupbox = QGroupBox()
            lbl = QLabel()
            lbl.setText(user)
            self.users_layout.addWidget(lbl)
            base_layout = QGridLayout()
            self.graphs_layout.addLayout(base_layout)

            _ = 0
            for operation in operations:
                _ =_ + 1
                layout = QHBoxLayout()
                frame1 = QFrame()
                frame2 = QFrame()
                layout.addWidget(frame1)
                layout.addWidget(frame2)
                base_layout.addLayout(layout, _ , 2)

    users = result[3]
    machines = result[4]

    BarSetsUsers = {}
    BarSetsMachines = {}

    for user in users:

        BarSets[user] = QBarSet(user)
        BarSets[user].append([])

    for machine in machines:

        BarSetsMachines[machine] = QBarSet(machine)
        BarSetsMachines[machine].append([])
    print(BarSetsUsers, BarSetsMachines)

    for user in users:

        hours = self.parser.hours_from_user(user)


def convert_sec_to_time(self, seconds) -> str:

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

def clearLayout(self, layout):

  while layout.count():

    child = layout.takeAt(0)

    if child.widget():

      child.widget().deleteLater()

def open_login_widget(self):

    self.login_widget = LoginWindow(self.users_db, self)
    self.login_widget.show()
    self.login_widget.submit_button.clicked.connect(self.click_check)

def open_timers_table(self):

    self.timers_table = TimersWindow(self.timers_db)
    self.timers_table.user = self.user
    print(self.user)
    self.timers_table.show()
