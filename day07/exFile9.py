"""
파일명 : exFile9.py 
프로그램 설명 : 파일 입출력 예제 (바이너리 파일 복사)
"""

# with문을 사용하지 않은 경우
# filename1 = 'calc.exe'
# filename2 = 'calc2.exe'
# f1 = open(filename1, 'rb')  # 원본 파일
# f2 = open(filename2, 'wb')  # 복사본 파일

# f2.write(f1.read())

# f1.close()
# f2.close()

# with문을 사용한 경우
filename1 = 'calc.exe'
filename2 = 'calc2.exe'
with open(filename1,"rb") as f1:
    with open(filename2,"wb") as f2:
        f2.write(f1.read())