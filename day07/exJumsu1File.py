"""
파일명 : exJumsu1File.py
프로그램 설명 : 성적처리 프로그램을 파일로 저장하기
"""

# 1. 점수 입력
print("점수를 입력하세요.")
kor  = input("국어 점수 : ")
eng  = input("영어 점수 : ")
math = input("수학 점수 : ")

# 2. 점수 체크
kor  = int(kor)  if kor.isdigit()  else 0
# if kor.isdigit():
#     kor  = int(kor)  
# else:
#     kor = 0   
eng  = int(eng)  if eng.isdigit()  else 0
math = int(math) if math.isdigit() else 0

# 3. 점수 계산
total = kor + eng + math  # 총점 
#total = sum([kor, eng, math])  # 총점  
average = total / 3  # 평균 

# 4. 점수 출력
print("===== 점수의 결과 =====\n"
      f"국어 점수 : {kor}\n"
      f"영어 점수 : {eng}\n"
      f"수학 점수 : {math}\n"
      f"총점 : {total}\n"
      f"평균 : {average:.2f}\n"
      "===== 점수의 결과 =====")

# 5. 파일 저장
filename="exJumsu1File.txt"

# with문을 사용하지 않은 경우
# f1=open(filename,"at",encoding='utf8')
# f1.write("===== 점수의 결과 =====\n"
#       f"국어 점수 : {kor}\n"
#       f"영어 점수 : {eng}\n"
#       f"수학 점수 : {math}\n"
#       f"총점 : {total}\n"
#       f"평균 : {average:.2f}\n"
#       "===== 점수의 결과 =====")

# with문을 사용한 경우
with open(filename,"at",encoding='utf8') as f1:
    f1.write("===== 점수의 결과 =====\n"
      f"국어 점수 : {kor}\n"
      f"영어 점수 : {eng}\n"
      f"수학 점수 : {math}\n"
      f"총점 : {total}\n"
      f"평균 : {average:.2f}\n"
      "===== 점수의 결과 =====\n\n")