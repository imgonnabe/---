"""
파일명: exBreak.py
프로그램 설명: break문
"""

# break  # SyntaxError: 'break' outside loop

i=1
while i<=5:
    print(i)
    i+=1
    if i==3:
        break

i=1
while i<=10:
    if i % 2 ==0:
        print(i)
        if i==4:
            break
    i+=1
print('프로세스 종료')
