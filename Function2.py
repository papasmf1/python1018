# Function2.py 
#정의되지 않은 인자 처리
#파이썬에서 사용하는 네이밍룰
#함수나 메서드는 카멜 표기법: userURL(), getProducts() 
#변수명: strURL  
#클래스명 파스칼 표기법: DemoProduct, DemoCustomer 각 단어의 첫글자를 대문자로 표현 
#파이썬 내부에 있는 멤버들: __변수명__ (앞뒤에 더블언더바) 스페셜한 멤버들(object)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출 
print( userURIBuilder("naver.com","80", id="kim", password="1234") )
print( userURIBuilder("naver.com","80", id="kim", password="1234", 
    name="mike") )

#메모리에 있는 내용들 딕셔너리 형태로 보기 
print( globals() )

#람다함수:이름이 없는 간결한 함수 정의
g = lambda x,y:x*y
print( g(3,4) )
print( (lambda x:x*x)(3) )
print( globals() )

