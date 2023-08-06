"""
파일명 : exForFor.py
프로그램 설명 : 중첩 for문
"""

for i in range(1,6):
    for j in range(6,11):
        print(i,j)
    else:
        print('j문 종료')
else:
    print('i문 종료')
    