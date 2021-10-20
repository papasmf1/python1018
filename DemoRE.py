# DemoRE.py 
import re 

#특정한 규칙이 있는 패턴 검색 
#함정을 추가
result = re.search("[0-9]*th", "  39th")
print( result )
print( result.group() )

#다중 라인 주석: ctrl + / 
# result = re.match("[0-9]*th", "  39th")
# print( result )
# print( result.group() )

print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )

print("---우편번호 검색---")
print( bool(re.search("\d{5}", "우리 동네는 52100")) )
result = re.search("\d{5}", "우리 동네는 52100")
print( result.group() )

