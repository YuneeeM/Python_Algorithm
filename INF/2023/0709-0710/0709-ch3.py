'''
조건문 if(분기, 중첩)

== 같다
!= 깉지 않다
'''

x = 7
if x == 7:
    print("Lucky")
    print("ㅋㅋ")  # 조건문에서 들여쓰기는 상당하게 중요함

# 중첩 조건문

x = 15
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")

x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")

x = 10
if x > 0:
    print("양수")
else:
    print("음수")

x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")
