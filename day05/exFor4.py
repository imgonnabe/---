"""
파일명 : exFor4.py
프로그램 설명 : continue, break
"""

for i in range(1,10):
    if i%2:
        if i==7:
            break
        continue
    print(i)
else:
    print('for문 종료')
print('프로세스 종료')

