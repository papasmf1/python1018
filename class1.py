# class1.py 
# 1)클래스 형식 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

# 2)인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"
p1.print() 
p2.print() 

#런타임(코드가 실행중)시에 변수를 추가(동적인 형식의 언어)
#디자인타임(코딩하는 중)
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )


