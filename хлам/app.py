import os
from PyQt5 import uic, QtWidgets
import ctypes
import sys

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'~qgis directory\apps\Qt5\plugins'
os.environ['PATH'] += r';~qgis directory\apps\qgis\bin;~qgis directory\apps\Qt5\bin'
sys.path.extend([r'~qgis directory\apps\qgis\python',r'~qgis directory\apps\Python37\Lib\site-packages'])
Ui_MainWindow, _ = uic.loadUiType("dialog.ui")

MY_COMPANY = "rudie"
MY_PRODUCT = "Hot-line my dairy"
MY_SUBPRODUCT = "calendar"
VERSION = "0.1"

def MakeMyAppOfficial() -> None:
    """With this strange code we're able to set custom icon in a task bar.
        For further reading: https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105
    """

    myappid = '.'.join((MY_COMPANY, MY_PRODUCT, MY_SUBPRODUCT, VERSION)) # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'{}'.format(myappid))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == '__main__':

    # Entry point
    MakeMyAppOfficial()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    app.exec_()