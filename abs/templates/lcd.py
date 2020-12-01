# color_event.py
# Import necessary modules
import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class SendSignal(QObject):
    """
    Define a signal change_style that takes no arguments.
    """
    change_style = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Create Custom Signals')
        self.setupLabel()
        self.show()

    def setupLabel(self):
        """
        Create label and connect custom signal to slot.
        """

        self.index = 0 # index of items in list
        self.direction = ""
        self.colors_list = ["red", "orange", "yellow", "green", "blue","purple"]

        self.label = QLabel()
        self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))
        self.setCentralWidget(self.label)

        # Create instance of SendSignal class, and
        # connect change_style signal to a slot.
        self.sig = SendSignal()
        self.sig.change_style.connect(self.changeBackground)

    def keyPressEvent(self, event):
        """
        Reimplement how the key press event is handled.
        """

        if event.key() == Qt.Key_Up:
            self.direction = "up"
            self.sig.change_style.emit()
        elif event.key() == Qt.Key_Down:
            self.direction = "down"
            self.sig.change_style.emit()

    def changeBackground(self):
        """
        Change the background of the label widget when a keyPressEvent
        signal is emitted.
        """
        if self.direction in ['up', 'down']:
            rgb = [random.randint(0, 256) for _ in range(3)]
            rgba = tuple(rgb + [150])
            self.label.setStyleSheet(f"background-color: rgba{rgba};")
            # rgba(0, 255, 255, 90)
        # if self.direction == "up":
        #     if self.index < len(self.colors_list) - 1:
        #         new_index = self.index + 1
        #     else:
        #         new_index = 0
        #     self._index_changed(new_index)
        #
        # elif self.direction == "down":
        #     new_index = self.index - 1 if self.index > 0 else len(self.colors_list) - 1
        #     self._index_changed(new_index)

    def _index_changed(self, new_index: int) -> None:
        self.index = new_index
        self.label.setStyleSheet("background-color: {}; opacity: 10%;".format(self.colors_list[self.index]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())
