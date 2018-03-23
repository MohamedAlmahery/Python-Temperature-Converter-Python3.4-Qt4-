# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Temperature Converter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from About import Ui_Dialog
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

class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(438, 333)
        Form.setMaximumSize(QtCore.QSize(438, 333))
        Form.setMouseTracking(True)
        icon = QtGui.QIcon('icons\icon.png')
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/D:/Barmaga/Icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"background:#272b38;\n"
"background-color:#272b38;\n"
"font-size:16px;\n"
"color:#FFF;\n"
"}\n"
"QPushButton{\n"
"color:#FFF;\n"
"background:#e30000;\n"
"border-radius:3px;\n"
"border-bottom:4px solid #aa0000;\n"
"}\n"
"QPushButton:pressed{\n"
"background:#aa0000;\n"
"border-radius:3px;\n"
"border:1px solid #aa0000\n"
"}\n"
"QPushButton:hover{\n"
"background:#750000;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#1abc9c;\n"
"}\n"
"QLineEdit\n"
"{\n"
"font:12pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:1px solid #aa0000;\n"
"padding:5px;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:1px solid #f80000;\n"
"}\n"
""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 281, 41))
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: rgb(161, 161, 0);\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.FlineEdit = QtGui.QLineEdit(Form)
        self.FlineEdit.setGeometry(QtCore.QRect(110, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FlineEdit.setFont(font)
        self.FlineEdit.setObjectName(_fromUtf8("FlineEdit"))
        self.ClineEdit = QtGui.QLineEdit(Form)
        self.ClineEdit.setGeometry(QtCore.QRect(110, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ClineEdit.setFont(font)
        self.ClineEdit.setObjectName(_fromUtf8("ClineEdit"))
        self.KlineEdit = QtGui.QLineEdit(Form)
        self.KlineEdit.setGeometry(QtCore.QRect(110, 190, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.KlineEdit.setFont(font)
        self.KlineEdit.setObjectName(_fromUtf8("KlineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 140, 121, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 200, 121, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 80, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 270, 231, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{\n"
"color:#FFF;\n"
"background:#00bd00;\n"
"border-radius:3px;\n"
"border-bottom:4px solid #55ff00;\n"
"}\n"
"QPushButton:pressed{\n"
"background:#55ff00;\n"
"border-radius:3px;\n"
"border:1px solid #55ff00\n"
"}\n"
"QPushButton:hover{\n"
"background:#226600;\n"
"}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(360, 250, 71, 71))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icons/icon.png")))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 51, 41))
        self.label_6.setStyleSheet(_fromUtf8("QLabel{\n"
"color: rgb(0, 255, 255);\n"
"}"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Temperature Converter", None))
        self.label.setText(_translate("Form", "Enter Go to = Temperature Converter", None))
        self.label_2.setText(_translate("Form", "Fahrenheit :", None))
        self.label_3.setText(_translate("Form", "Celsius      :", None))
        self.label_4.setText(_translate("Form", "Kelvin        :", None))
        self.FlineEdit.setPlaceholderText(_translate("Form", "Fahrenheit", None))
        self.ClineEdit.setPlaceholderText(_translate("Form", "Celsius", None))
        self.KlineEdit.setPlaceholderText(_translate("Form", "Kelvin", "enter go"))
        self.pushButton_2.setText(_translate("Form", "Go", None))
        self.pushButton_3.setText(_translate("Form", "Go", None))
        self.pushButton.setText(_translate("Form", "Go ", None))
        self.pushButton_4.setText(_translate("Form", "Click Here", None))
        self.label_6.setText(_translate("Form", "About ", None))
    # interact with the widgets
    def setup_events(self, Form):
        self.pushButton.clicked.connect(self.f_convert)
        self.pushButton_2.clicked.connect(self.c_convert)
        self.pushButton_3.clicked.connect(self.k_convert)
        self.FlineEdit.returnPressed.connect(self.f_convert)
        self.ClineEdit.returnPressed.connect(self.c_convert)
        self.KlineEdit.returnPressed.connect(self.k_convert)
        self.pushButton_4.clicked.connect(self.Aboutshow)
        
    # display changes
    def Aboutshow(self):
        self.About = QtGui.QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.About)
        self.About.show()
        
    
    def f_convert(self):
        words = self.FlineEdit.text()
        try:
            ftemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.ClineEdit.setText('')
            self.KlineEdit.setText('')
            return
        self.change_message('clear')
        self.ClineEdit.setText('%.2f' % self.f_to_c(ftemp))
        self.KlineEdit.setText('%.2f' % self.c_to_k(self.f_to_c(ftemp)))
        return
    
    def c_convert(self):
        words = self.ClineEdit.text()
        try:
            ctemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.FlineEdit.setText('')
            self.KlineEdit.setText('')
            return
        self.change_message('clear')
        self.FlineEdit.setText('%.2f' % self.c_to_f(ctemp))
        self.KlineEdit.setText('%.2f' % self.c_to_k(ctemp))
        return
    
    def k_convert(self):
        words = self.KlineEdit.text()
        try:
            ktemp = float(words)
        except (ValueError, TypeError):
            self.change_message('error')
            self.FlineEdit.setText('')
            self.ClineEdit.setText('')
            return
        self.change_message('clear')
        self.FlineEdit.setText('%.2f' % self.c_to_f(self.k_to_c(ktemp)))
        self.ClineEdit.setText('%.2f' % self.k_to_c(ktemp))
        return
    
    def change_message(self, status):
        messages = {'error': 'I don\'t understand your input.', 'clear': 'By : Python Temperature Converter'}
        self.label.setText(_translate('Form', messages[status], None))

    # conversion math
    def f_to_c(self, temp):
        return (temp - 32) * 5 / 9
    
    def c_to_f(self, temp):
        return temp * 9 / 5 + 32
    
    def c_to_k(self, temp):
        return temp + 273.15
    
    def k_to_c(self, temp):
        return temp - 273.15


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.setup_events(Form)
    Form.show()
    sys.exit(app.exec_())

