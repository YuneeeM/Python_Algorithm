'''
변수입력과 연산자
'''

a = input()  # 입력값 넣을 수 있음
print(a)

a = input("숫자를 입력하세요: ")
print(a)

a, b = input("숫자를 입력하세요 : ").split()  # 문자형 연결
print(a+b)
c = a+b
print(type(a))
print(type(c))

a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)  # 한방에 정수형으로 바꿀 수 있는 방법

'''
// = 몫
% = 나머지
** = 거듭제곱
'''

a = 4.3
b = 5
c = a+b
print(type(c))  # 실수형임
