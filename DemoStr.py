# DemoStr.py 

#print( dir(str) )

#반복되는 문자열 만들기
names = ["전우치","홍길동","이순신"]
for name in names:
    print("안녕하세요. {0}님 추운 겨울입니다.".format(name))
    print("=" * 40)

strData = "python is very powerful"
print( len(strData) )
print( strData.capitalize() )
print( strData.count("p") )
#count("패턴", start, end)
print( strData.count("p", 7) )

print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

print("---끝부분 패턴---")
print( "demo.ppt".endswith("ppt") )

print("---문자열 가공---")
strData2 = "<<<  spam and ham  >>>"
print(strData2)
print( strData2.strip("<> ") )
result = strData2.strip("<> ")
result = result.replace("spam", "spam egg")
print( result )
print("---리스트로 받기---")
lst = result.split() 
print( lst )
print("---문자열로 합치기---")
result2 = " ".join(lst)
print( result2 )

