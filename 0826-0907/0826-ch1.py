import sys
from collections import deque
sys.stdin = open("0826/input1.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)
'''
동적계획법이란? 네트워크 선 자르기(Bottom-Up)

현수는 네트워크 선을 1m,2m의 길이를 갖는 선으로 자르려고 함

'''
n = int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n])
