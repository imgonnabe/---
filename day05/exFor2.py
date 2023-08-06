"""
파일명 : exFor2.py
프로그램 설명 : for문 
"""

def myFunction():
    return (1,2,3,4,5)

# for문 옆에 올 수 있는 iterator object 살펴보기
print(iter([1,2,3,4,5]))  # <list_iterator object at 0x0000028E6004B688>
print(iter((1,2,3,4,5)))  # <tuple_iterator object at 0x0000028E6004B688>
print(iter("12345"))      # <str_iterator object at 0x0000028E6004B688>
print(iter(range(1,6)))   # <range_iterator object at 0x0000028E5FB9E770>
print(iter(myFunction())) # <tuple_iterator object at 0x0000028E6004BA88>
print(iter({1,2,3,4,5}))  # <set_iterator object at 0x0000028E60045A98>
print(iter({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})) # <dict_keyiterator object at 0x0000028E60045A98> 