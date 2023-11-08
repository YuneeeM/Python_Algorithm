import sys
import random as r
sys.stdin = open("0718/input7.txt", "rt")  # 파일 읽어오기

'''
창고정리

가장 높은 곳과 낮은 곳의 차이 출력하기

'''

L = int(input())

box = list(map(int, input().split()))

box.sort()

M = int(input())
s = 0
e = L-1

for _ in range(M):
    box[s] += 1
    box[e] -= 1
    box.sort()

# print(max(box)-min(box))
print(box[L-1]-box[0])
