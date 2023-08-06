# 파일명: myMax.py
# 함수명: myMax
# 인수: 값 2개
# 첫 번째 매개변수명: a
# 두 번째 매개변수명: b
# 리턴값: 두 개의 값을 비교해서 가장 큰 값을 리턴한다.
# 기능: 전달된 인수값을 비교해서 가장 큰 값을 돌려준다.

def myMax(a,b):
    if a>b:
        return a
    else:
        return b

# print(myMax(1,2))    # 2
# print(myMax(100,2))  # 100
# print(myMax(100,2,200))  # 에러 (인수를 2개밖에 받을 수 없다.)

# 여러 개의 인수를 받을 때는 매개변수를 *args로 받으면 된다.
def function(*args):
    print(args,type(args))
function(1,2)
function(1,2,3)
function(1,2,3,4,5)

def myMax(*args):
    a=0
    for b in args:
        if a>b:
            a=a
        else:
            a=b
    return a

print(myMax(1,2))
print(myMax(100,2))
print(myMax(100,2,200))