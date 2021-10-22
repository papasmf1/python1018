# DemoButton.py
# Qt디자이너를 사용하지 않고 맨땅에 헤딩하는 스타일의 코드 
# 100% 코드로 접근하면 유지보수 하기에 편하다. 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        #X축과 Y축을 셋팅 
        btn1.move(0, 20)
        #시그널과 슬롯 메서드 연결 
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 