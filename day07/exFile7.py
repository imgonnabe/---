"""
파일명 : exFile7.py 
프로그램 설명 : 파일 입출력 예제 (인코딩 utf8 형식으로 파일에 데이터 읽기)
"""

filename="exFile6.txt"
# 전통적인 방법의 파일 읽기
# f=open(filename,"rt",encoding="utf8")
# data=f.readline()
# while data:
#     print(data,end="")
#     data=f.readline()
# f.close()

# 전통적인 방법의 파일 읽기를 with문을 이용해서 변경한 경우
# with open(filename,"rt",encoding="utf8") as f:
#     data=f.readline()
#     while data:
#         print(data,end="")
#         data=f.readline()

# for문을 이용해서 좀 더 심플하게 반복해서 처리하는 경우
with open(filename,"rt",encoding="utf8") as f:
    for data in f:
        print(data,end="")

# readlines()를 이용한 경우
# with open(filename,"rt",encoding="utf8") as f:
#     data=f.readlines()
#     for line in data:
#         print(line,end="")
# print(type(data))
