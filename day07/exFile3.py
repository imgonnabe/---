"""
파일명 : exFile3.py 
프로그램 설명 : 파일 입출력 예제 (파일 포인터)
"""

filename="exFile1.txt"
f=open(filename,"r")
# 파일 포인터: 파일의 위치를 가지고 있는 포인터
# 파일일 열고 읽거나 쓰면 파일 포인터는 자동으로 이동된다. (파이썬에서 자동으로 설정된다.)
# print(f.read(1))  # H
# print(f.read(1))  # e
# print(f.read(1))  # l
# print(f.read(1))  # l
# print(f.read(1))  # o
# print(f.read(1))  # x

# 파일 포인터: 파일의 위치를 가지고 있는 포인터
# print(f.read(2))  # He
# print(f.read(2))  # ll
# print(f.read(1))  # o

# while문을 이용해서 출력한다.
# data = f.read(1)
# while data:
#     print(data,end="")
#     data=f.read(1)

# 무한루프를 이용해서 출력한다.
# while 1: #while True:
#     data=f.read(1)
#     if data:
#         print(data,end="")
#     else:
#         break

# while 1:
#     data=f.read(1)
#     if not data:
#         break
#     print(data,end="")

count=1
data=f.read(1)
while data:
    print(count," ", end="")
    print(data)
    data=f.read(1)
    count+=1
f.close()
    