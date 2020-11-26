import pyuic5 
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn1 = QPushButton('Ок', self)
        self.btn1.move(60, 60)
        self.btn1.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Авторизация')
        self.show()


    def showDialog(self):

        text1, ok = QInputDialog.getText(self, 'Input Dialog',
            'Имя пользователя:')

        if ok:
            self.le.setText(str(text))
            
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

