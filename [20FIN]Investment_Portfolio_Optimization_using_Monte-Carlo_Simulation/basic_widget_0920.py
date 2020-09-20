import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):

        #super 인 QMainWindow의 instance variable 다 가져옴
        super().__init__()

        #kiwoom widget 프로그램 import
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        #window 설정
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150)
        
        #Update weight 버튼
        btn1 = QPushButton("Update_Weight", self)
        btn1.move(30, 20)
        btn1.clicked.connect(self.btn1_clicked)

        #Update rebalance 버튼
        btn2 = QPushButton("Rebalance", self)
        btn2.move(150, 20)
        btn2.clicked.connect(self.btn2_clicked)

        #표시 정보창
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("logged in")
    
    def btn1_clicked(self):
        # weight calc function import
        pass
    
    def btn2_clicked(self):
        # rebalancing function import
        pass

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
