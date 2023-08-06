"""
파일명 : exFor1.py
프로그램 설명 : for문 
"""

# for i in range(5):
# for i in range(1,6):
# for i in (1,2,3,4,5):
for i in 'Hello':
    print(i)
else:
    print('for문 종료')

dictData={'a':1,'b':2,'c':3,'d':4,'e':5}
for i in dictData:
    print(i)
    print(dictData[i])

def myFunction():
    return (1,2,3,4,5)
print(myFunction())
for i in myFunction():
    print(i)