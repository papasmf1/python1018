# Function1.py 
#함수를 먼저 정의
def setValue(a):
    x = a 
    print(x)

#함수를 호출
result = setValue(5)
print( result )

def swap(x,y):
    return y,x

#호출
print( swap(5,6) )

print("---불변형식과 가변형식---")
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#기본값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자(파라메터명 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자(입력 파라메터 갯수가 변경되는 경우)
def union(*ar):
    #지역변수 
    result = []
    #단어를 슬라이싱 
    for item in ar:
        #각 글자를 슬라이싱 
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )
