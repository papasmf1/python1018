# DemoDB.py 
import sqlite3

#파일을 먼저 생성(일단은 메모리에서 미리 연습)
con = sqlite3.connect(":memory:")
#SQL구문을 실행할 커서 객체 생성
cur = con.cursor() 
#데이터 구조 만들기(테이블 스키마)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

#결과 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


