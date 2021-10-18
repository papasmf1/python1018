# DemoDict.py 
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( device )
print( len(device) )
print( device["아이폰"] )
device["맥프레"] = 15 
device["아이폰"] = 6 
print( device )
del device["아이폰"]
#중단점(Break Point):디버깅하는 모드에서는 멈춤
for item in device.items():
    print(item)

print("---key, value---")
for k,v in device.items():
    print(k,v)


phone = {"kim":"1111", "lee":"2222"}
#참조를 복사해서 전달 
p = phone 
print( id(phone), id(p) )


#교집합을 구하는 함수 
def intersect(prelist, postlist):
    #함수 내부에만 있는 지역변수 
    result = []
    #단어의 글자를 슬라이싱하는 코드: H(0) | A(1) | M(2)
    for x in prelist:
        #postlist에 있고 result에는 없는 글자면 추가 
        if x in postlist and x not in result:
            result.append(x)
    #루프 다 돌고 나서 리턴 
    return result 

#함수 호출
#중단점(Break Point)
print( intersect("HAM", "SPAM") )


