"""
파일명: 함수6.py
프로그램 설명: 함수 예제
"""

# 함수 정의
def functionTest1():
    """정수 자료형을 리턴하는 경우"""
    return 3.14
print(functionTest1,type(functionTest1()))

def functionTest2():
    """실수 자료형을 리턴하는 경우"""
    return 3.14
print(functionTest2,type(functionTest2()))

def functionTest3():
    """리스트 자료형을 리턴하는 경우"""
    return [1,2,3,4,5]
print(functionTest3(), type(functionTest3()))

def functionTest4():
    """튜플 자료형을 리턴하는 경우"""
    return (1,2,3,4,5)
    # return 1,2,3,4,5
print(functionTest4(), type(functionTest4()))

def functionTest5():
    """딕셔너리 자료형을 리턴하는 경우"""
    return {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(functionTest5(), type(functionTest5()))

def functionTest6():
    """셋 자료형을 리턴하는 경우"""
    return {1, 2, 3, 4, 5}
print(functionTest6(), type(functionTest6()))

def functionTest7():
    """불리언 자료형을 리턴하는 경우"""
    return True
print(functionTest6(), type(functionTest6()))