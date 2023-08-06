"""
파일명: exMembership1.py
프로그램 설명: 멤버십 연산자 예제1
"""

# number 변수에 1~5까지 저장한다.
number=[1,2,3,4,5]

# 반복이 가능한지 확인한다.
print(iter([]),iter(number))

# number 변수에 5가 존재합니까?
print(5 in number)

# number 변수에 13이 존재합니까?
print(13 in number)

# number 변수에 7이 존재하지 않습니까?
print(7 not in number)

# number 변수에 13이 존재하지 않습니까?
print(13 not in number)

a=int(input('입력: '))
print(a==1 or a==2 or a==3)
print(a in (1,2,3))
