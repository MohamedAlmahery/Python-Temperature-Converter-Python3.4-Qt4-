# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(396, 437)
        icon = QtGui.QIcon('icons\icon.png')
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/D:/Barmaga/Icons/Hopstarter-3d-Cartoon-Vol3-Axialis-Icon-Workshop.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.Link)
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 70, 361, 351))
        self.stackedWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.textEdit = QtGui.QTextEdit(self.page)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 341, 321))
        self.textEdit.setFrameShadow(QtGui.QFrame.Raised)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(70, 130, 231, 191))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/Dapino-Office-Women-Eyes-office-women-purple.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def Link(self, Dialog):
        import webbrowser
        webbrowser.open('https://www.facebook.com/MuhamedAshrafofficial/')
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.commandLinkButton.setText(_translate("Dialog", "To {Help} Face Book | Page : Muhammad Ashraf", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Name : </span><span style=\" font-size:8pt; font-weight:600; color:#7bb900;\">Muhammad Ashraf </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Egyptian</span><span style=\" font-size:8pt; font-weight:600; color:#c17825;\"> </span><span style=\" font-size:8pt; font-weight:600; color:#550000;\">Devoloper</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#0000ff;\">Computer Programmer &amp; Android Devoloper </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#8743cb;\">Call Me : </span><span style=\" font-size:9pt; font-weight:600; color:#55557f;\">+</span><span style=\" font-size:9pt; font-weight:600; color:#373753;\">201142174779</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

