"""
파일명 : errorTest.py
프로그램 설명 : print() 함수와 에러 구분하기
"""

# print() : 문자열이나 값을 출력할 때 사용하는 함수다.
# 함수 : 명령어
# 문자열 : 문자들이 여러개 모여있는 것을 말한다.
# 문자열을 사용할 때는 따옴표(작은,큰)로 묶어서 사용한다.
# 형식 : print(변수), print(문자열)
print('오늘은 파이썬을 배웁니다.')
print("오늘은 파이썬을 배웁니다.")

# 파이썬에 자주 접하는 에러 확인
# 1. 문법이 틀린 경우
# SyntaxError: 에러의 원인이 출력된다.
# print(Hello world!)
# print("Hello world!")
#
# 2. 들여쓰기가 잘못된 경우
# IndentationError: 에러의 원인이 출력된다.
#  print("Hello world!")
#
# 3. 이름이 잘못된 경우
# NameError: 에러의 원인이 출력된다.
# prin("Hello world!")

print("프로그램 종료")