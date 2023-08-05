"""
파일명 : exDict1.py
프로그램 설명: 딕셔너리 자료형
"""

# d 변수에 1 ~ 5까지 저장한다.
d={'a':1,'b':2,'c':3,'z':4,'y':5}
print(d,type(d))

# 딕셔너리는 Sequence 타입의 객체가 아니므로 순서를 가지고 있지 않다.
# 그러므로 리스트나, 튜플처럼 index인 변수명[0] 처럼 값에 접근할 수 없다.
# 편법을 쓰면 가능하다. 키를 숫자로 지정하면 된다.
# print(d[0])  # KeyError: 0

# 편법으로 번호로 지정한 경우(index 번호의 효과)
dictData2 = {0:1, 1:2, 2:3, 3:4, 4:5}
print(dictData2, type(dictData2))  # {0: 1, 1: 2, 2: 3, 3: 4, 4: 5} <class 'dict'>
print(dictData2[0])  # key를 index 처럼 사용할 수 있다. (비추)

# 딕셔너리에 저장된 데이터에 접근하기 위해서는 키로 접근해야 한다.
# 형식 : 변수명['키'], 변수명[변수]
# 변수에 방을 번호(리스트, 튜플)로 표현하는 것이 아니라 이름(딕셔너리)으로 표현한다.
print(d['a'])
a='z'
print(d[a])

# 변수를 이용하는 방법
dictData = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
key = ['a', 'b', 'c', 'd', 'e']
print(dictData[key[0]])  # 1 변수 key[0]에 저장된 값이 키가 된다.
print(dictData[key[1]])  # 2 변수 key[1]에 저장된 값이 키가 된다.
print(dictData[key[2]])  # 3 변수 key[2]에 저장된 값이 키가 된다.
print(dictData[key[3]])  # 4 변수 key[3]에 저장된 값이 키가 된다.
print(dictData[key[4]])  # 5 변수 key[4]에 저장된 값이 키가 된다.

# 반복성
# 딕셔너리 자료형은 반복성을 가지고 있으므로 for문으로 돌릴 수 있다.
dictData = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# 딕셔너리는 for문에서 키를 던진다.
for value in dictData:
    print(value)

# key 변수에 저장된 키의 값을 이용해서 값을 출력한다.
for value in dictData:
    print(dictData[value])

# 딕셔너리에서 메소드(메서드)를 이용해서 key를 추출한다.
for key in dictData.keys():
    print(key)

# 딕셔너리에서 메소드(메서드)를 이용해서 값을 추출한다.
for value in dictData.values():
    print(value)

# 학생의 정보를 저장하는 변수를 사전 자료형으로 생성한다.
# 저장되는 값: 이름(name), 핸드폰(phone), 생일(birth)
student = {'name':'홍길동', 'phone':'010-1111-2222', 'birth':'12월25일'}

print(student['name'])
print(student['phone'])
print(student['birth'])
print()
