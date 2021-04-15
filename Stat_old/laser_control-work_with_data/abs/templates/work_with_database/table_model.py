import sys
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QTableView,
                            QVBoxLayout, QMessageBox, QHeaderView)

from PyQt5.QtSql import (QSqlDatabase, QSqlTableModel, QSqlQuery,
                        QSqlRelationalTableModel, QSqlRelation)


class TableDisplay(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setMinimumSize(1000, 500)
        self.setWindowTitle('SQL Table Model')
        self.createConnection()
        self.createTable()
        self.show()

    def createConnection(self):
        """
        Set up the connection to the self.db.
        Check for the tables needed.
        """

        self.db = QSqlDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('pyqt5_test_db')
        self.db.setUserName('postgres')
        self.db.setPassword('ghbdtnlfnf')


        # database = QSqlself.db.addDatabase("QSQLITE")
        # self.db.setDatabaseName(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_self.db.db"))

        if not self.db.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {'accounts'}

        tables_not_found = tables_needed - set(self.db.tables())
        if tables_not_found:
            QMessageBox.critical(None, 'Tables not found', f'Tables does not exist:\n{", ".join(tables_not_found)}')
            sys.exit(1) # Error code 1 – signifies error

    def createTable(self):
        """
        Create the table using model/view architecture.
        """

        # Create the model
        model = QSqlTableModel(db=self.db)
        model.setTable('accounts')
        # model.setQuery(QSqlQuery("SELECT id FROM accounts", db=self.db))
        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Populate the model with data
        model.select()

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)


class RelationalTableDisplay(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """

        self.setMinimumSize(1000, 500)
        self.setWindowTitle('Relational Table Model')
        self.createConnection()
        self.createTable()
        self.show()

    def createConnection(self):
        """
        Set up the connection to the database.
        Check for the tables needed.
        """

        self.db = QSqlDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('pyqt5_test_db')
        self.db.setUserName('postgres')
        self.db.setPassword('ghbdtnlfnf')

        if not self.db.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {'accounts', 'countries'}
        tables_not_found = tables_needed - set(self.db.tables())

        if tables_not_found:
            QMessageBox.critical(None, 'Error', f'The following tables are missing from the database: {", ".join(tables_not_found)}')
            sys.exit(1) # Error code 1 – signifies error

    def createTable(self):
        """
        Create the table using model/view architecture.
        """

        # Create the model
        model = QSqlRelationalTableModel(db=self.db)
        model.setTable('accounts')
        # Set up relationship for foreign keys
        model.setRelation(model.fieldIndex('country_id'), QSqlRelation('countries', 'id', 'country'))
        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.
        Stretch)
        # Populate the model with data
        model.select()
        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = RelationalTableDisplay()

    sys.exit(app.exec_())
