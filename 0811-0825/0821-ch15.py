import sys
from collections import deque
sys.stdin = open("0811/input15.txt", "rt")  # 파일 읽어오기

'''
토마토(BFS 활용)
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 
토마토의 영향을 받아 익게 된다.
 현수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
정수 1  익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않음
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

Q = deque()
dis = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]]+1
            Q.append((xx, yy))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
