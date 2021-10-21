# form1.py 
# form1.ui(화면단) + form1.py(로직을 수행)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("form1.ui")[0]

#윈도우클래스를 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#진입점을 체크(직접 모듈을 실행했는지 여부)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm() 
    demoWindow.show()
    app.exec_() 
