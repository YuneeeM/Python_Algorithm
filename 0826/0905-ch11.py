import sys
from collections import deque
sys.stdin = open("0826/input11.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
동전교환
다음과 같이 여러 단위의 동전들이 주어져 있을 때 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 주면 되는가?
'''

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000]*(m+1)
dy[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        dy[j] = min(dy[j], dy[j-coin[i]]+1)

print(dy[m])
