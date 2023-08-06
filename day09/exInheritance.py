"""
파일명 : exInheritance.py 
프로그램 설명 : 상속
"""

# class A(Object):
class A:
    a = 1
    
    def methodA(self): 
        print("methodA() 실행!")

class B(A):
    b = 2

    def methodB(self):
        print('methodB() 실행!')

objb = B()
print(objb.a, objb.b)
objb.methodA()
objb.methodB()
print("프로세스 종료")