from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import sys


class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):

        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        palette = qApp.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):

        texts = []

        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res



class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.comunes = ['Ameglia', 'Arcola', 'Bagnone', 'Bolano', 'Carrara', 'Casola', 'Castelnuovo Magra',
            'Comano, località Crespiano', 'Fivizzano', 'Fivizzano località Pieve S. Paolo',
            'Fivizzano località Pieve di Viano', 'Fivizzano località Soliera', 'Fosdinovo', 'Genova',
            'La Spezia', 'Levanto', 'Licciana Nardi', 'Lucca', 'Lusuolo', 'Massa', 'Minucciano',
            'Montignoso', 'Ortonovo', 'Piazza al sercho', 'Pietrasanta', 'Pignine', 'Pisa',
            'Podenzana', 'Pontremoli', 'Portovenere', 'Santo Stefano di Magra', 'Sarzana',
            'Serravezza', 'Sesta Godano', 'Varese Ligure', 'Vezzano Ligure', 'Zignago' ]

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        self.combo_box = CheckableComboBox(self)
        self.combo_box.setGeometry(200, 150, 150, 30)
        # geek list
        # adding list of items to combo box
        self.combo_box.addItems(self.comunes)

        # create label to show to text

        # setting geometry of label



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())


# creating checkable combo box class
# class CheckableComboBox(QComboBox):
#
# 	def __init__(self):
#
# 		super(CheckableComboBox, self).__init__()
#
# 		self.view().pressed.connect(self.handle_item_pressed)
# 		self.setModel(QStandardItemModel(self))
#
# 	# when any item get pressed
# 	def handle_item_pressed(self, index):
#
# 		# getting which item is pressed
# 		item = self.model().itemFromIndex(index)
#
# 		# make it check if unchecked and vice-versa
# 		if item.checkState() == Qt.Checked:
# 			item.setCheckState(Qt.Unchecked)
# 		else:
# 			item.setCheckState(Qt.Checked)
#
# 		# calling method
# 		self.check_items()
#
# 	# method called by check_items
# 	def item_checked(self, index):
#
# 		# getting item at index
# 		item = self.model().item(index, 0)
#
# 		# return true if checked else false
# 		return item.checkState() == Qt.Checked
#
# 	# calling method
# 	def check_items(self):
# 		# blank list
# 		checkedItems = []
#
# 		# traversing the items
# 		for i in range(self.count()):
#
# 			# if item is checked add it to the list
# 			if self.item_checked(i):
# 				checkedItems.append(i)
#
# 		# call this method
# 		self.update_labels(checkedItems)
#
# 	# method to update the label
# 	def update_labels(self, item_list):
#
# 		n = ''
# 		count = 0
#
# 		# traversing the list
# 		for i in item_list:
#
# 			# if count value is 0 don't add comma
# 			if count == 0:
# 				n += ' % s' % i
# 			# else value is greater then 0
# 			# add comma
# 			else:
# 				n += ', % s' % i
#
# 			# increment count
# 			count += 1
#
#
# 		# loop
# 		for i in range(self.count()):
#
# 			# getting label
# 			text_label = self.model().item(i, 0).text()
#
# 			# default state
# 			if text_label.find('-') >= 0:
# 				text_label = text_label.split('-')[0]
#
# 			# shows the selected items
# 			item_new_text_label = text_label + ' - selected index: ' + n
#
# 		# setting text to combo box
# 			self.setItemText(i, item_new_text_label)
#
# 	# flush
# 	sys.stdout.flush()
#
#
# class Window(QMainWindow):
#
# 	def __init__(self):
# 		super(QMainWindow, self).__init__()
#
# 		# creating a widget object
# 		myQWidget = QWidget()
# 		# vertical box layout
# 		myBoxLayout = QVBoxLayout()
# 		myQWidget.setLayout(myBoxLayout)
# 		# central widget
# 		self.setCentralWidget(myQWidget)
# 		# creating checkable combo box
# 		self.ComboBox = CheckableComboBox()
# 		# traversing items
# 		for i in range(3):
# 			# adding item
# 			self.ComboBox.addItem("Combobox Item " + str(i))
# 			item = self.ComboBox.model().item(i, 0)
#
# 			# setting item unchecked
# 			item.setCheckState(Qt.Unchecked)
#
# 		# adding combo box to the layout
# 		myBoxLayout.addWidget(self.ComboBox)
#
# # drivers code
# if __name__ == '__main__':
#
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	window.resize(480, 320)
# 	sys.exit(app.exec_())
