import sys

sys.stdin = open("0808/input14-1.txt", "rt")  # 파일 읽어오기

'''
인접행렬(가중치 그래프)
첫째 줄에는 정점의 수와 간선의 수가 주어짐
'''
n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
