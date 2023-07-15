import sys
import random as r
sys.stdin = open("0715/input3.txt", "rt")  # 파일 읽어오기

'''
카드 역배치
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한줄로 놓여 있음
이제 카드의 위치를 바꿈 구간 [a,b] 1<=a<=b<=20가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓음

#swap방식
a, b = map(int, input().split())
print(a, b)
a, b = b, a
print(a, b)


'''
a = list(range(21))

# _변수가 없는것
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)

for x in a:
    print(x, end=" ")
