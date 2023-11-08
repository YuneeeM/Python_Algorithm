import sys
from collections import deque
sys.stdin = open("0826/input15.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
위상정렬(그래프 정렬)

위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘
각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를
유지하면서 전체 일의 순서를 짜는 알고리즘이다.
'''
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)  # 진입차수
dQ = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1
for i in range(1, n+1):
    if degree[i] == 0:
        dQ.append(i)
while dQ:
    x = dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dQ.append(i)
