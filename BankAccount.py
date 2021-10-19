# BankAccount.py

#파이썬은 개인적으로 사용:AI, 데이터 사이언스, 분석 
#팀단위로 작업할 경우: 멤버 숨김 
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #이름숨김: 복잡한 이름으로 변경해 달라~~ 
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #문자열로 결과를 출력
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, 
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)
#print(account1.__balance)
#변경된 이름(백도어)
print(account1._BankAccount__balance)
