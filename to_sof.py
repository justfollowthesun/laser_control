class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MoveableWidget):
    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.parser = DataParser()
        self.create_table()

    def create_table(self):

        header_font = QFont('Sergoe UI', 12)
        header_font.setWeight(QFont.Bold)

        self.tableWidget.setColumnCount(3)

        self.tableWidget.setHorizontalHeaderLabels([ "Относительное время","Абсолютное время", "Название операции"])
        self.tableWidget.horizontalHeaderItem(0).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(1).setFont(header_font)
        self.tableWidget.horizontalHeaderItem(2).setFont(header_font)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)

        list_to_add = self.parser.parsing() #[operation date, operation name, status]
        print(list_to_add)

        rowPos = self.tableWidget.rowCount()

        date_now = datetime.now()
        datetime_event = datetime.strptime(list_to_add[0], '%Y-%m-%d %H:%M:%S')
        print(datetime_event)
        print(date_now)
        delta_sec = (datetime.now() - datetime_event).total_seconds()
        print(delta_sec)
        time_abs = self.convert_sec_to_time(delta_sec)

        self.tableWidget.insertRow(rowPos)

        self.tableWidget.setItem(rowPos, 2, QTableWidgetItem(list_to_add[1]))
        self.tableWidget.setItem(rowPos, 1, QTableWidgetItem(time_abs))
        self.tableWidget.setItem(rowPos, 0, QTableWidgetItem("Text in column 3"))

def initate_application() -> None:


    if platform.system() == 'Windows':
        set_current_process_explicit_attributes()

    main_widget = MainWindow()
    main_widget.show()
    app.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    initate_application()
