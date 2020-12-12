from PyQt5 import QtWidgets, uic, QtChart,QtCore
from datetime import datetime
from config import UI_MAIN_WINDOW, DESIGN_DIR
from storage.database import Database
from widgets.login_widget import LoginWindow
from model.table_window import TableModel
from abs.templates.spreadsheet import SpreadsheetTemplate
from abs.templates.plotting.qtchart import PieChartConstructor
from utils.input_data_imit import generate_data_flow

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW, import_from=DESIGN_DIR)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    employee=[]
    def __init__(self, database: Database) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.table = SpreadsheetTemplate()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.database = database
        #self.login_widget = LoginWindow(self.database,self)
        #self.login_widget.show()

        self.diagram=self.create_piechart()
        #self.show()
        self.setCentralWidget(self.diagram)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.recieve_data)
        # update the timer every tenth second
        timer.start(1000)
        self.gen=generate_data_flow()
        self.show()

    def closeEvent(self, event) -> None:
        event.accept()

    def create_piechart(self) -> QtChart.QChartView:

        series = QtChart.QPieSeries()

        [series.append(*piece) for piece in [('value', 100),]]

        pie = PieChartConstructor(series)
        pie.add_slice(0)

        return pie

    def recieve_data(self):
        #print(next(self.gen))
        try:
            a=next(self.gen)
        except StopIteration:
            self.gen=generate_data_flow()
            a=next(self.gen)

        if  a[1]=='START':
            if a[2] not in self.employee:
                self.diagram.series.append(QtChart.QPieSlice(a[2],50))
                self.employee.append(a[2])
            else:
                for slice in self.diagram.series.slices():
                    if slice.label()==a[2]:
                        slice.setValue(slice.value()*2)
