import sys
import random as r
sys.stdin = open("0715/input4.txt", "rt")  # 파일 읽어오기

'''
두 리스트 합치기
오름차순으로 정렬이 된 리스트가 주어지면 두 리스트를 오름차순으로 합쳐
출력하는 프로그램
'''
a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))


p1 = p2 = 0  # 포인터 변수

s = []

while p1 < a and p2 < c:
    if b[p1] <= d[p2]:
        s.append(b[p1])
        p1 += 1
    else:
        s.append(d[p2])
        p2 += 1
if p1 < a:
    s = s+b[p1:]
if p2 < c:
    s = s+d[p2:]

for x in s:
    print(x, end=" ")
