import re 

#로그파일을 읽기
f=open('c:\\work\\PV3.txt','rt')
#필요한 내용만 복사 
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("error", line.lower() )):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








