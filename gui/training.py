"""from PyQt4.QtGui import *
 
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
         
        # 레이블,Edit,버튼 컨트롤       
        btn_navigation = QPushButton("Navigation Mode")
        self.editName = QLineEdit()
        btn_mapping = QPushButton("Map edit mode")
 
        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(btn_navigation)
        layout.addWidget(btn_mapping)
         
        # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)

        #버튼 클릭시 연결
        btn_navigation.clicked.connect(self.btn_navigation_clicked)

    def btn_navigation_clicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "Info", name)
 
# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()
"""


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

class MyCustomWidget(QWidget):
    def __init__(self,parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QHBoxLayout()
        self.row.addWidget(QPushButton("add"))
        self.setLayout(self.row)

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent=parent)
        vLayout = QtGui.QVBoxLayout(self)
        hLayout = QtGui.QHBoxLayout()
        self.lineEdit = QtGui.QLineEdit()
        hLayout.addWidget(self.lineEdit)
        self.filter = QtGui.QPushButton("filter", self)
        hLayout.addWidget(self.filter)
        self.list = QtGui.QListView(self)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.list)
        self.model = QtGui.QStandardItemModel(self.list)
        codes = [
            'windows',
            'windows xp',
            'windows7',
            'hai',
            'habit',
            'hack',
            'good'
        ]
        self.list.setModel(self.model)
        for code in codes:
            item = QtGui.QStandardItem(code)
            self.model.appendRow(item)
            self.list.setIndexWidget(item.index(), QtGui.QPushButton("button"))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())