"""
파일명: exWhile3.py
프로그램 설명: while문을 이용한 로그인 프로그램
"""

import getpass
userid='pythonuser'
userpw='123456'

print('>>>로그인<<<')

i=1
while i<=3:
    inputUserid=input('사용자: ')
    inputUserpw=getpass.getpass('비밀번호: ')
    if userid==inputUserid and userpw==inputUserpw:
        print('로그인 성공!')
        print(f'{userid}님 환영합니다.')
        break
    else:
        
        print('로그인 실패!')
    i+=1
else:
    print('프로그램 종료')
    exit()
print('로그인 후 실행되는 코드가 온다.')