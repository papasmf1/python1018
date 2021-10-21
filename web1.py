# web1.py 
from bs4 import BeautifulSoup

#웹페이지를 로딩
#메서드나 함수를 메서드체인(연속으로 호출)
page = open("c:\\work\\test01.html", encoding="utf-8").read()
#검색이 용이한 객체(html태그 문서를 검색-상수)
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#<p> 몽땅 검색
print( soup.find_all("p") )

