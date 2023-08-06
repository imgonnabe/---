"""
파일명 : exInheritance.py 
프로그램 설명 : 메소드 오버라이딩(메소드 재정의)
"""

class A:
    a = 1
    
    def methodA(self): 
        print("methodA() 실행!")

class B(A):
    b = 2

    def methodA(self): 
        print(">>> methodA() 재정의 실행! <<<")
        
    def methodB(self):
        print('methodB() 실행!')    

    def methodC(self):
        super().methodA()

objb = B()
print(objb.a, objb.b)  # 1 2
objb.methodA()
objb.methodB()
objb.methodC()
print('프로세스 종료 ') 