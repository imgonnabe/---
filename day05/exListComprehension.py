"""
파일명 : exListComprehansion.py
프로그램 설명 : 리스트 컴프리헨션
"""

# 리스트 컴프리헨션을 사용하지 않은 경우
a = []
for i in range(1,6):
    a.append(i)
print(a)

# 리스트컴프리헨션을 사용해서 값을 추가한 경우 
# 변수명 = [실행문 for문]
a=[i for i in range(1,6)]
print(a)

# 형식 : 변수명 = [실행문 for문]
listData1=[i for i in range(1,6)]
print(listData1)
listData1=[i*2 for i in range(1,6)]
print(listData1)

# 형식 : 변수명 = [실행문 for문 if문]
# listData2=[]
# for i in range(1,11):
#     if i%2==0:
#         listData2.append(i)
listData2=[i for i in range(1,11) if i%2==0]
print(listData2)

# 형식 : 변수명 = [실행문 if 조건식 else 실행문 for문 ]
# listData3=[]
# for i in range(1,11):
#     if i%2==0:
#         listData3.append(i)
#     else:
#         listData3.append(i+100)
# print(listData3)
listData3=[i if i%2==0 else i+100 for i in range(1,11)]
print(listData3)

listData4=[i if i%3==0 else i+1 for i in range(1,11)]
print(listData4)