# web2.py 
#웹서버에 요청 
import urllib.request
#검색 
from bs4 import BeautifulSoup



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
print("웹 크롤링 종료~~")

