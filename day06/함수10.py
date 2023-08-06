"""
파일명: 함수10.py
프로그램 설명: 함수 예제
"""

value=1

# 함수 내부에서 전역변수 읽기 
# 함수 내부에서 전역변수 value에 접근할 수 있다.
# r(읽기) 가능하다.
def printValue():
    print(value, type(value))

printValue()

# 함수 내부에서 전역변수 쓰기 
# 함수 내부에서 전역변수 value에 접근해서 저장한다.
# w(쓰기) 불가능하다.
def changeValue():
    value = 10
    print(value, type(value))

changeValue()
print(value)   