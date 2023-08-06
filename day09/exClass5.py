"""
파일명 : exClass5.py 
프로그램 설명 : 소멸자 사용하기 
"""

# 소멸자는 객체가 없어질 때 자동으로 호출되는 메소드
# 소멸자는 값을 삭제할 때 사용한다.
# 소멸자는 생성자처럼 __del__ 로 이름이 정해져 있다.
# 리소스를 해제할 때 사용된다.

class ClassTest5:
    def __init__(self, name):
        """생성자"""
        self.name = name
        print(f'{self.name} 생성자 실행')

    def __del__(self):
        """소멸자"""
        print(f'{self.name} 소멸자 실행!')

ct51 = ClassTest5('홍길동')
del ct51
ct52 = ClassTest5('고길동')
ct53 = ClassTest5('김길동')

# 실행 결과
# 홍길동 생성자 실행!
# 홍길동 소멸자 실행!
# 고길동 생성자 실행!
# 김길동 생성자 실행!
# 고길동 소멸자 실행!
# 김길동 소멸자 실행!