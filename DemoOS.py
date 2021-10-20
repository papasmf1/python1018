# DemoOS.py 
from os.path import * 

#print( dir() )

print( abspath("python.exe") )
print( basename("c:\\python38\\python.exe") )
print( getsize("c:\\python38\\python.exe") )
print( exists("c:\\python38\\python.exe") )

#운영체제에 있는 기능 접근: cd \ cd work 
from os import * 
#운영체제 이름과 환경변수
print( name )
print( environ.keys() )
print( getcwd() )
chdir("..")
print( getcwd() )
chdir("c:\\work")
#특정 프로그램 실행
#system("notepad.exe")

#dir, ls 명령어 
import glob 
result = glob.glob("c:\\work\\*.*") 
for item in result:
    print(item)






