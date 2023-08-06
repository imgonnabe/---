"""
파일명: exWhile2.py
프로그램 설명: while문
"""

# 반복문을 사용하지 않고 5 ~ 1까지 출력
i = 5
print(i)  # 5
i -= 1
print(i)  # 4
i -= 1
print(i)  # 3
i -= 1
print(i)  # 2
i -= 1
print(i)  # 1


# 반복문을 사용하고 5 ~ 1까지 출력
i=5
while i>=1:
    print(i)
    i-=1
else:
    print('while문 종료')

# 감소하면서 5번 이름을 출력한다.
i=5

# 반복문을 사용하고 5 ~ 1까지 출력
while i>=1:
    print('홍길동')
    i-=1
else:
    print('while문 종료')

# 증가하면서 5번 이름을 출력한다.
i = 1

# 반복문을 사용하고 1 ~ 5까지 출력
while i<=5:
    print('홍길동')
    i+=1
else:
    print('while문 종료')