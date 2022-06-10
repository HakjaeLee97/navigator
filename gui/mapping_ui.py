# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapping_ui.ui'
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
        Dialog.resize(600, 1024)
        Dialog.setStyleSheet(_fromUtf8("background-color:rgb(250, 250, 250)"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 800, 120, 50))
        self.pushButton.setStyleSheet(_fromUtf8("border:None;\n"
"background-color:rgb(42,42,42);color:rgb(255,255,255);\n"
"font:24pt \"맑은 고딕\";\n"
"border-radius:10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 800, 120, 50))
        self.pushButton_2.setStyleSheet(_fromUtf8("border:None;\n"
"background-color:rgb(42,42,42);color:rgb(255,255,255);\n"
"font:24pt \"맑은 고딕\";\n"
"border-radius:10px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 800, 120, 50))
        self.pushButton_3.setStyleSheet(_fromUtf8("border:None;\n"
"background-color:rgb(42,42,42);color:rgb(255,255,255);\n"
"font:24pt \"맑은 고딕\";\n"
"border-radius:10px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open_image_btn)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.save_btn)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close_btn)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "열기", None))
        self.pushButton_2.setText(_translate("Dialog", "저장", None))
        self.pushButton_3.setText(_translate("Dialog", "닫기", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

