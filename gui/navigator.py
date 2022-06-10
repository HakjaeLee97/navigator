#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
#from dest_list_ui import Ui_Form

#import navigator_ui
#import dest_list_ui
import dest_list_ui2


#class XDialog(QDialog, navigator_ui.Ui_Dialog):
    # def __init__(self):
    #     QDialog.__init__(self)
    #     # setupUi() 메서드는 화면에 다이얼로그 보여줌
    #     self.setupUi(self)
        

    # def navigate_mode(self):
    #     #목적지 리스트 켜기
    #     dest_list_dialog.show()

    # def map_edit_mode(self):
    #     #맵 에딧 모드 켜기
        
    #     #QtGui.QFileDialog.getOpenFileName()
    #     #meg.show()
    #     img_layout.show()

# class listDialog(QWidget, dest_list_ui.Ui_Form):
#     #목적지 선택 gui
#     def __init__(self):
#         super(listDialog, self).__init__()
#         self.lay = QtGui.QHBoxLayout()
#         self.sA = QtGui.QScrollArea()

#         self.sA_Lay = QtGui.QVBoxLayout()
#         self.sA.setLayout(self.sA_Lay)
#         self.lay.addWidget(self.sA)
#         self.setLayout(self.lay)
#         #QWidget.__init__(self)
#         # setupUi() 메서드는 화면에 다이얼로그 보여줌
#         self.setupUi(self)    
#     def add_list_item(self,button_name):
        
#         button = QtGui.QPushButton(button_name)
#         self.sA_Lay.addWidget(button)
#         return

#     def home(self):
#         pass
    


class dest_list_dialog(QWidget, dest_list_ui2.Ui_Form):
    #목적지 선택 gui
    def __init__(self):
        super(dest_list_dialog, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.lay = QtGui.QHBoxLayout()
        self.sA = QtGui.QScrollArea()

        #self.sA_Lay = QtGui.QVBoxLayout()
       # self.sA.setLayout(self.sA_Lay)
       # self.lay.addWidget(self.sA)
        #self.setLayout(self.lay)
        #QWidget.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)    
    def add_list_item(self,button_name):
        
        button = QtGui.QPushButton(button_name)
        self.sA_Lay.addWidget(button)
        return



    def hide_arrow(self):
        #화살표를 숨기는 메소드. 다른 화살표를 띄우기 전에 실행
        try:
            self.lbl.hide()

        except:
            pass
    def hide_text(self):
        #텍스트를 숨기는 메소드. 남은 거리를 바꾸기 전에 실행
        try:
            self.lbl_text.hide()

        except:
            pass

    def print_arrived(self):
        #"도착" 글씨를 띄우는 메소드
        self.lbl = QLabel(self)
        self.lbl.resize(600,800)  
        pixmap = QPixmap("text_arrive.png")
        self.lbl.setPixmap(pixmap)
        
        #self.lbl.resize(400,300)
        self.lbl.show()          

    def print_right_arrow(self):
        #오른쪽 화살표 띄우는 메소드
        self.lbl = QLabel(self)
        self.lbl.resize(600,800)  
        pixmap = QPixmap("arrow_right.png")
        self.lbl.setPixmap(pixmap)
        
        #self.lbl.resize(600,1024)  
        self.lbl.show()       


    def print_left_arrow(self):
        #왼쪽 화살표 띄우는 메소드
        self.lbl = QLabel(self)
        self.lbl.resize(600,800)  
        pixmap = QPixmap("arrow_left.png")
        self.lbl.setPixmap(pixmap)
        #self.lbl.setGeometry()
        #self.lbl.resize(600,1024)  
        self.lbl.show() 

    def print_straight_arrow(self):
        #직진 화살표 띄우는 메소드
        self.lbl = QLabel(self)
        self.lbl.resize(600,800)   # 이미지를 보여주기 위해 출력될 label의 크기를 400×400으로 설정
        #self.lbl.setGeometry(200,200,600,600)
        pixmap = QPixmap("arrow_straight.png")
        self.lbl.setPixmap(pixmap)
        
        #self.lbl.resize(600,1024)   # 이미지를 보여주기 위해 출력될 창의 크기를 400×400으로 설정
        self.lbl.show() 

    def print_meter_text(self,meter):
        self.lbl_text = QLabel(self)
        self.lbl_text.resize(300,50)
        text_to_print = str(meter) +"m"
        text_to_print = text_to_print.decode('utf-8')
        self.lbl_text.setText(text_to_print)
        self.lbl_text.setFont(QtGui.QFont("맑은고딕",48))
        self.lbl_text.setGeometry(240,750,300,50)
        self.lbl_text.show()

    def home(self):
        #홈버튼이 눌렸을 때 할 행동
        self.hide_arrow()
        self.hide_text()
        pass

    def btn1(self):
        #버튼1이 눌렸을 때 할 행동 
        print('btn1 clicked')
        self.print_left_arrow()
        pass

    def btn2(self):
        #버튼 2가 눌렸을 때 할 행동
        self.print_arrived()
        pass

    def btn3(self):
        #버튼 3이 눌렸을 때 할 행동
        
        self.print_right_arrow()
        self.print_meter_text(30)
        pass

    def btn4(self):
        #버튼 4가 눌렸을 때 할 행동
        self.print_straight_arrow()
        
class CustomWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.button = QtGui.QPushButton("buttaon")
        lay = QtGui.QHBoxLayout(self)
        lay.addWidget(self.button, alignment=QtCore.Qt.AlignRight)
        lay.setContentsMargins(0, 0, 0, 0)

class Dialog_list(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog_list, self).__init__(parent=parent)
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
            self.list.setIndexWidget(item.index(), CustomWidget())

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.list = QtGui.QListWidget(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.list)

    def addListItem(self, text):
        item = QtGui.QListWidgetItem(text)
        self.list.addItem(item)
        widget = QtGui.QWidget(self.list)
        button = QtGui.QToolButton(widget)
        layout = QtGui.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.list.setItemWidget(item, widget)
        button.clicked[()].connect(
            lambda: self.handleButtonClicked(item))

    def handleButtonClicked(self, item):
        print(item.text())

class TestGui(QtGui.QWidget):
    """ A Fast test gui show how to create buttons in a ScrollArea"""
    def __init__(self):
        super(TestGui, self).__init__()
        self.lay = QtGui.QHBoxLayout()
        self.sA = QtGui.QScrollArea()
        self.sA.widgetResizable = False
        self.sA_lay = QtGui.QHBoxLayout()
        self.sA.setLayout(self.sA_lay)
        self.sA.setGeometry(QtCore.QRect(220,40,641,471))
        self.sA.setWidgetResizable(True)
        self.closeGui = QtGui.QPushButton("Close")
        self.add_file_button = QtGui.QPushButton("Add File")
        self.lay.addWidget(self.closeGui)
        self.lay.addWidget(self.add_file_button)
        self.lay.addWidget(self.sA)
        self.setLayout(self.lay)
        self.connect_()

    def connect_(self):
        self.add_file_button.clicked.connect(self.__add_file_to_list)
        self.closeGui.clicked.connect(self.close)
        return

    def __add_file_to_list(self,button_name):
        fname = QtGui.QFileDialog.getOpenFileName()
        global filenames
        filenames.append(fname)
        button = QtGui.QPushButton(fname)
        button.setMinimumSize(QtCore.QSize(0,450))
        
        self.sA_lay.addWidget(button)
        return


class Map_edit_gui(QtGui.QWidget):

    def __init__(self):
        super(Map_edit_gui, self).__init__()
        self.lay = QtGui.QHBoxLayout()
        self.sA = QtGui.QScrollArea()
        self.sA_lay = QtGui.QVBoxLayout()
        self.sA.setLayout(self.sA_lay)
        self.closeGui = QtGui.QPushButton("Close")
        self.add_file_button = QtGui.QPushButton("Add File")
        self.lay.addWidget(self.closeGui)
        self.lay.addWidget(self.add_file_button)
        self.lay.addWidget(self.sA)
        self.setLayout(self.lay)
       # self.connect_()

    #def connect_(self):
     #   self.add_file_button.clicked.connect(self.__add_file_to_list)
      #  self.closeGui.clicked.connect(self.close)
       # return

    def __add_file_to_list(self,button_name):
        fname = QtGui.QFileDialog.getOpenFileName()
        #global filenames
        #filenames.append(fname)
        button = QtGui.QPushButton(button_name)
        self.sA_lay.addWidget(button)
        return

class img_lay(QMainWindow):
    def __init__(self):
        super(img_lay,self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(400,400)   # 이미지를 보여주기 위해 출력될 label의 크기를 400×400으로 설정
        pixmap = QPixmap("aa.png")
        self.lbl.setPixmap(pixmap)

        self.resize(400,400)   # 이미지를 보여주기 위해 출력될 창의 크기를 400×400으로 설정
        #self.show()

class dest_arrow_lay(QMainWindow):
    def __init__(self):
        super(dest_arrow_lay,self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(211,464)   # 이미지를 보여주기 위해 출력될 label의 크기를 400×400으로 설정
        pixmap = QPixmap("arrow.png")
        self.lbl.setPixmap(pixmap)

        self.resize(600,1024)   # 이미지를 보여주기 위해 출력될 창의 크기를 400×400으로 설정
        #self.show()        

class navigation_arrow(QtGui.QWidget):
    def __init__(self):
        super(navigation_arrow, self).__init__()
        img_widget = QWidget()
        img_widget.setWindowTitle("Navigating Mode")
        label = QLabel(img_widget)
        pixmap = QPixmap('./gui/grid_map.jpg')
        label.setPixmap(pixmap)
        img_widget.resize(pixmap.width(),pixmap.height()) 
        img_widget.show()       



if __name__ == "__main__":

    #initialize
    app = QApplication(sys.argv)
    
    #dlg = XDialog()
    meg = Map_edit_gui()
    img_layout = img_lay()
    arrow_dialog = dest_arrow_lay()
    dest_dialog = dest_list_dialog()
    
    dest_dialog.show()
    #dest_dialog.showMaximized()
    # 전체화면으로 실행 

    list_appendable = TestGui()
    #list_appendable.show()
    arr = navigation_arrow()
    #arr.show()
    #ad = listDialog()
    #for i in range(1,2):
    #    ad.add_list_item("asd")
   # ad.show()

    

    #dest_list_dialog.add_file_to_list("dest1")
    #dest_list_dialog.add_file_to_list("dest2")
    ##dest_list_dialog.add_file_to_list("dest3")
    #dest_list_dialog.add_file_to_list("dest4")
    #dlg.show()
    app.exec_()

    #sys.exit(app.exec_())

#
#길안내 화면
#목적지 선택

#목적지 입력k


#할일
#목적지 불러와서 버튼 만들고 스크롤
#점찍기
#우분투에 파이큐티 설치


#코너에서 좌회전 -> n미터 앞에서 
#인터넷 연결없을떄 돌아가게
#우분투 시작프로그램
#우분투 자동잠금
