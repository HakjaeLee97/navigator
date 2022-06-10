#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui 
#from PySide import QtCore, QtGui #Just tested it for PyQt4 since I don't have PySide installed...


class PaintTable(QtGui.QTableWidget):
    def __init__(self, parent):
        QtGui.QTableWidget.__init__(self, parent)
        self.center = QtCore.QPoint(-10,-10)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self.viewport()) #See: http://stackoverflow.com/questions/12226930/overriding-qpaintevents-in-pyqt
        painter.drawEllipse(self.center,10,10)
        QtGui.QTableWidget.paintEvent(self,event)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.center = QtCore.QPoint(event.pos().x(),  event.pos().y())
            print self.center
            self.viewport().repaint()

        elif event.buttons() == QtCore.Qt.LeftButton:
            QtGui.QTableWidget.mousePressEvent(self,event)

class MainWindow(PaintTable):
    def __init__(
        self,
        parent = None
    ):
        super(MainWindow, self).__init__(parent)

# General grid
        self.table = PaintTable(self)
        self.nbrow, self.nbcol = 9, 9
        self.table.setRowCount(self.nbrow)
        self.table.setColumnCount(self.nbcol)
        for row in range(0, self.nbrow):
            self.table.setRowHeight(row, 50)

            for col in range(0, self.nbcol):
                self.table.setColumnWidth(col, 50)

# Each cell contains one single QTableWidgetItem
        for row in range(0, self.nbrow):
            for col in range(0, self.nbcol):
                item = QtGui.QTableWidgetItem()
                item.setTextAlignment(
                    QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
                )

                self.table.setItem(row, col, item)

# Header formatting
        font = QtGui.QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        self.table.horizontalHeader().setFont(font)
        self.table.verticalHeader().setFont(font)

# Font used
        font = QtGui.QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(20)
        self.table.setFont(font)

# Global Size
        self.resize(60*9, 60*9 + 20)

# Layout of the table
        layout = QtGui.QGridLayout()
        layout.addWidget(self.table, 0, 0)
        self.setLayout(layout)

# Set the focus in the first cell
        self.table.setFocus()
        self.table.setCurrentCell(0, 0)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fen = MainWindow()
    fen.show()
    sys.exit(app.exec_())