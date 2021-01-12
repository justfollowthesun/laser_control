import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from typing import Optional


class TimerTemplate(QtWidgets.QWidget):

    _counter: int = 0
    _is_started: bool = False
    _default_timer_text: str = "Set new timer"
    _completed_timer_text: str = "Ding-dong"

    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_time)

        # update the timer every tenth second
        timer.start(100)

    def initializeUI(self) -> None:
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('A Simple Timer')
        self.setupWidgets()
        self.show()

    def setupWidgets(self) -> None:
        """
        Create widgets for timer GUI and arrange them in the window
        """
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(50, 5, 50, 5)

        self.clock_label = QtWidgets.QLabel(self._default_timer_text)
        self.clock_label.setFont(QtGui.QFont('Calibri', 15))
        self.clock_label.setMaximumSize(250, 50)
        self.clock_label.setAlignment(QtCore.Qt.AlignCenter)

        setup_timer_button = QtWidgets.QPushButton(self._default_timer_text)
        setup_timer_button.clicked.connect(self.setup_timer)

        self.action_button = QtWidgets.QPushButton("Start")
        self.action_button.clicked.connect(self.start_action)

        reset_button = QtWidgets.QPushButton("Reset")
        reset_button.clicked.connect(self.reset_action)

        layout.addWidget(self.clock_label)
        layout.addWidget(setup_timer_button)
        layout.addWidget(self.action_button)
        layout.addWidget(reset_button)

        self.setLayout(layout)

    def update_time(self) -> None:
        """
        A method called by QTimer every 1/10 seconds
        """

        if self._is_started:

            self._counter -= 1

            if self._counter != 0:
                text = str(self._counter / 10) + " s"
                self.clock_label.setText(text)
            else:
                self._is_started = False
                self.set_label_and_button_text(custom_label_text=self._completed_timer_text)


    def print_timer(self):

            if self._is_started:

                self._counter -= 1

                if self._counter != 0:
                    text = str(self._counter / 10) + " s"
                    self.clock_label.setText(text)
                else:
                    self._is_started = False
                    self.set_label_and_button_text(custom_label_text=self._completed_timer_text)

    def set_label_and_button_text(self, custom_label_text: Optional[str] = None) -> None:
        """
        Change clock_label and action_button text

        Args:
            custom_label_text (Optional[str]): . Defaults to _default_timer_text.

        """
        self.clock_label.setText(custom_label_text or self._default_timer_text)
        self.action_button.setText("Start")

    def setup_timer(self) -> None:
        """
        Create QInputDialog to set new timer
        """

        self._is_started = False

        seconds, set_new_timer = QtWidgets.QInputDialog.getInt(self, 'Set new timer', 'Enter Seconds:', min=1, max=1000, value=60)

        if set_new_timer:

            # Our timer is ticking with 1/10 second step
            self._counter = seconds * 10
            self.set_label_and_button_text(str(seconds))

    def start_action(self) -> None:
        """
        Called when self.action_button is pressed
        """

        if self._is_started:
            self._is_started = False
            self.action_button.setText("Start")
        else:
            if self._counter != 0:
                self.action_button.setText("Pause")

            self._is_started = self._counter != 0

    def reset_action(self) -> None:
        self._is_started = False
        self._counter = 0
        self.set_label_and_button_text()



# create pyqt5 app
App = QtWidgets.QApplication(sys.argv)

# create the instance of our Window
window = TimerTemplate()

# start the app
sys.exit(App.exec_())
