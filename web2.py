# web2.py 
#웹서버에 요청 
import urllib.request
#검색 
from bs4 import BeautifulSoup

#웹사이트에서 검색한 결과를 문자열로 받기
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 생성
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
#     <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri">격렬한 나의 하루</a>
# </td>
#조건을 주고 필터링
cartoons = soup.find_all("td", class_="title")
#10개를 가져왔다면 
print("갯수:{0}".format(len(cartoons)))
#첫번째 방에 있는 아이템 슬라이싱 
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print( title )
print( link )

