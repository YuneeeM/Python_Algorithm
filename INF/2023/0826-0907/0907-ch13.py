import sys
from collections import deque
sys.stdin = open("0826/input13.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
플로이드 워샬 알고리즘 ☆☆☆
N개의 도시가 주어지고, 각 도시들을 연결하는 도로와 해당 도로를 통행하는 비용이 주어질 
때 모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값을 구하는 프로그램
'''
n, m = map(int, input().split())
dis = [[5000]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])  # 중요한 알고리즘
for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == 5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
