import sys
import random as r
sys.stdin = open("0715/input7.txt", "rt")  # 파일 읽어오기

'''
사과나무(다이아몬드)
농장 n*n 격자판, 각 격자안에는 한 그루의 사과나무가 심어져 있음
n의 크기는 항상 홀수, 가을이 되어 사과 수확시 현수는 격자판안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 
나머지 격자안의 사과는 새들을 위해 남겨둠

'''

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
res = 0

s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
