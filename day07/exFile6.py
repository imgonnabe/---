"""
파일명 : exFile6.py 
프로그램 설명 : 파일 입출력 예제 (인코딩 utf8 형식으로 파일에 데이터 쓰기)
"""

filename = "exFile6.txt"
# 1. 파일 열기
# UTF8을 사용하기 위한 인수 encoding='utf8'
# 형식: 
# 변수명 = open('파일명', '열기모드', encoding='utf8') 
f=open(filename,"wt",encoding="utf8")

# 2. 파일 처리 (쓰기)
# 파일객체명.write("문자열")
# 리턴값: 파일에 쓴 문자열의 글자수를 반환한다.
# 언어셋이 UTF8이면 한글 한 글자에 3byte의 크기를 갖고
# 영문이나 공백, \n은 그대로 1byte 크기를 갖는다.
# Hello 안녕하세요. : 22byte
print(f.write("Hello 안녕하세요.")) # 글자수: 12개

# 3. 파일 닫기
f.close()

# utf8로 파일을 저장하면 utf8로 파일을 오픈해야 한다.
# utf8로 저장하고 cp949로 오픈하면 인코딩 에러가 발생한다.
with open(filename, 'r', encoding='utf8') as f:
    print(f.read())