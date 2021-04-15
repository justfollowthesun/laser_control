from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5 import QtWidgets
from abs.qt import MoveableWidget
from PyQt5.QtWidgets import QApplication
import sys
import platform
import socket
import codecs

class DataRecieve(QThread):

    signal_Data = pyqtSignal(['QString'])
    data_emit = pyqtSignal(list)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def parsing_message(self, message):

        msg_to_pars = codecs.decode(message, 'UTF-8')
        msg_to_pars = msg_to_pars[1 : -1]
        msg_to_list = msg_to_pars.split(',')
        data = []
        for msg in msg_to_list:
            msg = msg.split(':"')
            msg = msg[-1][0:-1]
            data.append(msg)
        return msg_to_pars

    def run(self):
        print(12345)
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 12345       # Port to listen on (non-privileged ports are > 1023)
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # s.bind((HOST, PORT))
                # s.listen()
                # msg_size = 0
                # print(123)
                # try:
                #     conn, addr = s.accept()
                # except KeyboardInterrupt:
                #     request.close()
                #     break
                # else:
                #     request = conn.recv(1024)
                #     if msg_size == 0:
                #         if len(request) < 2:
                #             pass
                #         else:
                #             len_message = int.from_bytes(request[:2], 'big')
                #             print(len_message)
                #             if len(request) < len_message:
                #                 pass
                #             else:
                #                 while len(request) >= len_message:
                #                     len_message = int.from_bytes(request[:2], 'big')
                #                     msg_to_pars = request[2:len_message+1]
                #                     data = self.parsing_message(msg_to_pars)
                #                     msg_size = 0
                #                     request = request[len_message+2:]
                #                     #self.data_emit.emit(data)
                #                     #self.signals.signal_Data.emit(msg_to_pars)
                #                     print('New message')
                #                     print('#########')
                data = 'string'
                self.signal_Data.emit(data)

class MainWindow(QtWidgets.QMainWindow,  MoveableWidget):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        self.add_data_thread = DataRecieve()
        self.add_data_thread.signal_Data.connect(self.on_Data)
        self.add_data_thread.start()

    @pyqtSlot(str)
    def on_Data(self, message):
        print(message)

def initate_application() -> None:


    main_widget = MainWindow()
    main_widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    initate_application()
    MW = MainWindow()
    MW.show()
