"""
파일명: ex05.py
프로그램 설명: 변수의 값 출력하기
"""
name='홍길동'
kor=100
eng=90
math=80
# print('이름:', name)     # 이름: 홍길동
# print('국어점수:', kor)   # 국어점수: 100
# print('영어점수:', eng)   # 영어점수: 90
# print('수학점수:', math)  # 수학점수: 80
# print(name, kor, eng, math) # 홍길동 100 90 80

# %용법 으로 출력한다.
# 형식 : print('서식 문자열' %(변수))
# %s: 문자열
# %d: 정수
print('이름: %s' %name)
print('국어점수: %d' %kor)
print('영어점수: %d' %eng)
print('수학점수: %d' %math)
print('%s %d %d %d' %(name,kor,eng,math))

# format() 메소드(함수) 용법으로 출력한다.
# 형식 : print('{}'.format(변수))
print('이름: {}'.format(name))
print('국어점수: {}'.format(kor))
print('영어점수: {}'.format(eng))
print('수학점수: '.format(math))
print('{} {} {} {}'.format(name,kor,eng,math))

# f-string 용법으로 출력한다.
# 형식 : print(f'{변수명}')
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {math}')
print(f'{name} {kor} {eng} {math}')
