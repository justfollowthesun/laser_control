import sys
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QComboBox, QTableView, QHeaderView,
                             QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox)

from PyQt5.QtSql import (QSqlDatabase, QSqlQuery,
                         QSqlRelationalTableModel, QSqlRelation,
                         QSqlRelationalDelegate)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class AccountManager(QWidget):

    db_fileds = ['id', 'employee_id', 'first_name', 'last_name', 'email', 'department', 'country_id']
    header = ["ID", "Employee ID", "First", "Last", "Email", "Dept.", "Country"]

    title_to_field = {
        "Sort by ID": "id",
        "Sort by Employee ID": "employee_id",
        "Sort by First Name": "first_name",
        "Sort by Last Name": "last_name",
        "Sort by Department": "department",
        "Sort by Country": "country"
    }

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setMinimumSize(1000, 600)
        self.setWindowTitle('10.1 – Account Management GUI')
        self.createConnection()
        self.createTable()
        self.setupWidgets()
        self.show()

    def createConnection(self):

        self.db = QSqlDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('pyqt5_test_db')
        self.db.setUserName('postgres')
        self.db.setPassword('ghbdtnlfnf')

        if not self.db.open():
            print("Unable to open data source file.")
            sys.exit(1)  # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {'accounts', 'countries'}
        tables_not_found = tables_needed - set(self.db.tables())

        if tables_not_found:
            QMessageBox.critical(
                None, 'Error', f'The following tables are missing from the database: {", ".join(tables_not_found)}')
            sys.exit(1)  # Error code 1 – signifies error

    def createTable(self):
        """
        Set up the model, headers and populate the model.
        """

        self.model = QSqlRelationalTableModel(db=self.db)
        self.model.setTable('accounts')
        self.model.setRelation(self.model.fieldIndex('country_id'), QSqlRelation('countries', 'id', 'country'))

        for header, field in zip(self.header, self.db_fileds):
            self.model.setHeaderData(self.model.fieldIndex(field),  Qt.Horizontal, header)

        # Populate the model with data
        self.setSortingOrder("Sort by ID")
        self.model.select()

    def setupWidgets(self):
        """
        Create instances of widgets, the table view and set layouts.
        """

        icons_path = "icons"
        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("font: bold 24px")
        add_record_button = QPushButton("Add Employee")
        add_record_button.setIcon(QIcon(os.path.join(icons_path, "add_user.png")))
        add_record_button.setStyleSheet("padding: 10px")
        add_record_button.clicked.connect(self.addRecord)
        del_record_button = QPushButton("Delete")
        del_record_button.setIcon(QIcon(os.path.join(icons_path, "trash_can.png")))
        del_record_button.setStyleSheet("padding: 10px")
        del_record_button.clicked.connect(self.deleteRecord)

        # Set up sorting combo box
        sorting_options = self.title_to_field.keys()

        sort_name_cb = QComboBox()
        sort_name_cb.addItems(sorting_options)
        sort_name_cb.currentTextChanged.connect(self.setSortingOrder)
        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_record_button)
        buttons_h_box.addWidget(del_record_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_name_cb)
        # Widget to contain editing buttons
        edit_buttons = QWidget()
        edit_buttons.setLayout(buttons_h_box)
        # Create table view and set model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        # Instantiate the delegate
        delegate = QSqlRelationalDelegate(self.table_view)
        self.table_view.setItemDelegate(delegate)
        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignLeft)
        main_v_box.addWidget(edit_buttons)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addRecord(self):
        """
        Add a new record to the last row of the table.
        """
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)
        id = 0
        query = QSqlQuery(db=self.db)
        query.exec_("SELECT max(id) FROM accounts")

        if query.next():
            id = int(query.value(0))

    def deleteRecord(self):
        """
        Delete an entire row from the table.
        """

        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())
            self.model.select()

    def setSortingOrder(self, text):
        """
        Sort the rows in table.
        """

        self.model.setSort(self.model.fieldIndex(self.title_to_field[text]), Qt.AscendingOrder)
        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AccountManager()
    sys.exit(app.exec_())
