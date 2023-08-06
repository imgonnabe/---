"""
파일명: exWhile1.py
프로그램 설명: while문
"""

# 반복문을 사용하지 않고 1 ~ 5까지 출력
i = 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)

# 반복문을 사용하고 1 ~ 5까지 출력
# 초기값 -> 조건식 -> 실행문 -> 증감식
i=1
while i<=5:
    print(i)
    i+=1
else:
    print('while문 종료')