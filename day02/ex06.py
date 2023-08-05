"""
파일명: ex06.py
프로그램 설명: print()함수의 다양한 사용법
"""

# print() 함수는 변수나 문자열을 화면에 출력하는 함수이다.
# 형식: print(value, ...)
# 형식: print(value, sep=' ')
# 형식: print(value, end='\n')
# print() 함수의 기본값 
# sep 변수 : ' '  <-- 공백
# end 변수 : '\n' <-- 엔터

i1=1
i2=2
i3=3

print(i1,i2,i3)
print(i1,i2,i3, sep='--', end='\n')
print(i1,i2,i3)