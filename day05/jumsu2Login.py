"""
파일명: jumsu2Login.py
프로그램 설명: 성적처리프로그램 + 로그인 기능 (입력 횟수: 3번)
"""

# 1. 로그인 기능
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
        print('아이디/비밀번호를 다시 확인해주세요!\n')
        i+=1
else:
    print('로그인 실패!')
    import sys
    sys.exit()
    
# 2. 입력 부분
name = input('이름: ')
kor  = int(input('국어점수: '))
eng  = int(input('영어점수: '))
math = int(input('수학점수: '))
# print(name, kor, eng, math)

# 3. 처리 부분
total = kor + eng + math
average = total / 3

# 4. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {math}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')