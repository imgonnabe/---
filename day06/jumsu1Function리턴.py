"""
파일명: jumsu1Function.py
프로그램 설명: 성적처리프로그램 
"""

# 함수 정의
def inputJumsu():

    # 1. 입력 부분
    name = input('이름: ')
    kor  = int(input('국어점수: '))
    eng  = int(input('영어점수: '))
    math = int(input('수학점수: '))
    # print(name, kor, eng, math)
    return name, kor, eng, math
    
def printJumsu(name, kor, eng, math):
    # 2. 처리 부분
    total = kor + eng + math
    average = total / 3

    # 3. 출력 부분
    print(f'이름: {name}')
    print(f'국어점수: {kor}')
    print(f'영어점수: {eng}')
    print(f'수학점수: {math}')
    print(f'총점: {total}')
    print(f'평균: {average:.2f}')

# 함수 호출
# retValue = inputJumsu()  # 리턴값을 하나의 변수로 받는다. (묶어서 받는다. 튜플)
# printJumsu(*retValue)    # 함수의 인수로 넘길 때 풀어서 넘긴다.
# retValue = inputJumsu()  묶어서 리턴하면 묶어서 받겠다.
# printJumsu(*retValue)    묶여 있는 것을 풀어서 던지겠다.

name, kor, eng, math = inputJumsu()  # 묶어서 리턴하면 풀어서 받겠다.
printJumsu(name, kor, eng, math)     # 변수를 각각 던지겠다.