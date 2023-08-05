# d={'이름':'홍길동','국어점수':100,'영어점수':99,'수학점수':98}
# print(d)

# total=d['국어점수']+d['수학점수']+d['영어점수']
# average=(d['국어점수']+d['수학점수']+d['수학점수'])/3
# print(total)
# print(average)

student={}

# 입력부분
student['name']=input('이름: ')
student['kor']=int(input('국어점수: '))
student['eng']=int(input('영어점수: '))
student['math']=int(input('수학점수: '))

# 2. 처리 부분
student['total']=student['kor']+student['eng']+student['math']
student['average']=student['total']/3

# 3. 출력 부분
print(f'이름: {student["name"]}')
print(f'국어점수: {student["kor"]}')
print('영어점수: %d' %student['eng'])
print(f'수학점수: {student["math"]}')
print(f'총점: {student["total"]}')
print(f'평균: {student["average"]:.2f}')

