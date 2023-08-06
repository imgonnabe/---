"""
파일명: exIdentity1.py
프로그램 설명 :  식별 연산자 예제 1
"""

# 파이썬에서는 모든 변수는 객체로 만든다.
# id() 함수: 변수의 메모리를 확일할 때 사용한다.
a1=7
a2=7
a3=8
print('a1',id(a1))
print('a2',id(a2))
print('a3',id(a3))

print(a1 is a2)
print(a1 is not a3)