# form2.py 
# form2.ui(화면단) + form2.py(로직을 수행)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹서버에 요청 
import urllib.request
#검색 
from bs4 import BeautifulSoup


#화면을 로딩(form2.ui로 변경)
form_class = uic.loadUiType("c:\\work\\form2.ui")[0]

#윈도우클래스를 정의(부모 클래스 변경: QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯 메서드 추가
    def firstClick(self):
        #파일에 저장하기
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        #수열을 만드는 함수
        for i in range(1,6):
            #기본 주소
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print("조립한주소:", url)
            #웹사이트에서 검색한 결과를 문자열로 받기
            data = urllib.request.urlopen(url)
            #검색이 용이한 객체 생성
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text
                print( title.strip() )
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText("웹 크롤룅 완료~~")

    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼클릭~~")


#인스턴스를 생성 
app = QApplication(sys.argv)
demoWindow = DemoForm() 
demoWindow.show()
app.exec_() 
