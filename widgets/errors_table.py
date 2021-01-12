from PyQt5 import QtWidgets, uic, QtCore
from config import UI_ERRORS_WINDOW, DESIGN_DIR
from abs.qt import MoveableWidget

from config import UI_ERRORS_WINDOW

Ui_ErrorsWindow, _ = uic.loadUiType(UI_ERRORS_WINDOW, import_from = DESIGN_DIR)

class ErrorsWindow(QtWidgets.QWidget, Ui_ErrorsWindow):

    def __init__(self) -> None:

        QtWidgets.QWidget.__init__(self)
        Ui_ErrorsWindow.__init__(self)
        self.setupUi(self)


    def closeEvent(self, event) -> None:
        dump_data(self)
        self.close()
