# form2.py 
# form2.ui(화면단) + form2.py(로직을 수행)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩(form2.ui로 변경)
form_class = uic.loadUiType("c:\\work\\form2.ui")[0]

#윈도우클래스를 정의(부모 클래스 변경: QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯 메서드 추가
    def firstClick(self):
        self.label.setText("첫번째 ~~")
    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼클릭~~")


#인스턴스를 생성 
app = QApplication(sys.argv)
demoWindow = DemoForm() 
demoWindow.show()
app.exec_() 
