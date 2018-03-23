
from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.setup_events(self)
    
    # set up the widgets
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 173)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.messageLabel = QtGui.QLabel(Form)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.verticalLayout.addWidget(self.messageLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.fLabel = QtGui.QLabel(Form)
        self.fLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLabel.setObjectName(_fromUtf8("fLabel"))
        self.verticalLayout_9.addWidget(self.fLabel)
        self.cLabel = QtGui.QLabel(Form)
        self.cLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cLabel.setObjectName(_fromUtf8("cLabel"))
        self.verticalLayout_9.addWidget(self.cLabel)
        self.kLabel = QtGui.QLabel(Form)
        self.kLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kLabel.setObjectName(_fromUtf8("kLabel"))
        self.verticalLayout_9.addWidget(self.kLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.fLineEdit = QtGui.QLineEdit(Form)
        self.fLineEdit.setObjectName(_fromUtf8("fLineEdit"))
        self.verticalLayout_8.addWidget(self.fLineEdit)
        self.cLineEdit = QtGui.QLineEdit(Form)
        self.cLineEdit.setObjectName(_fromUtf8("cLineEdit"))
        self.verticalLayout_8.addWidget(self.cLineEdit)
        self.kLineEdit = QtGui.QLineEdit(Form)
        self.kLineEdit.setObjectName(_fromUtf8("kLineEdit"))
        self.verticalLayout_8.addWidget(self.kLineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.fButton = QtGui.QPushButton(Form)
        self.fButton.setObjectName(_fromUtf8("fButton"))
        self.verticalLayout_5.addWidget(self.fButton)
        self.cButton = QtGui.QPushButton(Form)
        self.cButton.setObjectName(_fromUtf8("cButton"))
        self.verticalLayout_5.addWidget(self.cButton)
        self.kButton = QtGui.QPushButton(Form)
        self.kButton.setObjectName(_fromUtf8("kButton"))
        self.verticalLayout_5.addWidget(self.kButton)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.exitButton = QtGui.QPushButton(Form)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.verticalLayout.addWidget(self.exitButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    # tell the widgets what to do. punish disobedience.
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Temperature converter", None))
        self.messageLabel.setText(_translate("Form", "Enter a temperature and click Go.", None))
        self.fLabel.setText(_translate("Form", "Fahrenheit", None))
        self.cLabel.setText(_translate("Form", "Celsius", None))
        self.kLabel.setText(_translate("Form", "Kelvin", None))
        self.fButton.setText(_translate("Form", "Go", None))
        self.cButton.setText(_translate("Form", "Go", None))
        self.kButton.setText(_translate("Form", "Go", None))
        self.exitButton.setText(_translate("Form", "Exit", None))
        
    # interact with the widgets
    def setup_events(self, Form):
        self.fButton.clicked.connect(self.f_convert)
        self.cButton.clicked.connect(self.c_convert)
        self.kButton.clicked.connect(self.k_convert)
        self.fLineEdit.returnPressed.connect(self.f_convert)
        self.cLineEdit.returnPressed.connect(self.c_convert)
        self.kLineEdit.returnPressed.connect(self.k_convert)
        self.exitButton.clicked.connect(self.close)
        
    # display changes
    def f_convert(self):
        words = self.fLineEdit.text()
        try:
            ftemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.cLineEdit.setText('')
            self.kLineEdit.setText('')
            return
        self.change_message('clear')
        self.cLineEdit.setText('%.2f' % self.f_to_c(ftemp))
        self.kLineEdit.setText('%.2f' % self.c_to_k(self.f_to_c(ftemp)))
        return
    
    def c_convert(self):
        words = self.cLineEdit.text()
        try:
            ctemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.fLineEdit.setText('')
            self.kLineEdit.setText('')
            return
        self.change_message('clear')
        self.fLineEdit.setText('%.2f' % self.c_to_f(ctemp))
        self.kLineEdit.setText('%.2f' % self.c_to_k(ctemp))
        return
    
    def k_convert(self):
        words = self.kLineEdit.text()
        try:
            ktemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.fLineEdit.setText('')
            self.cLineEdit.setText('')
            return
        self.change_message('clear')
        self.fLineEdit.setText('%.2f' % self.c_to_f(self.k_to_c(ktemp)))
        self.cLineEdit.setText('%.2f' % self.k_to_c(ktemp))
        return
    
    def change_message(self, status):
        messages = {'error': 'I don\'t understand your input.', 'clear': ''}
        self.messageLabel.setText(_translate('Form', messages[status], None))

    # conversion math
    def f_to_c(self, temp):
        return (temp - 32) * 5 / 9
    
    def c_to_f(self, temp):
        return temp * 9 / 5 + 32
    
    def c_to_k(self, temp):
        return temp + 273.15
    
    def k_to_c(self, temp):
        return temp - 273.15

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
    return 0

if __name__ == '__main__':
    main()
