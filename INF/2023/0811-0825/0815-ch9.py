import sys
from collections import deque
sys.stdin = open("0811/input9.txt", "rt")  # 파일 읽어오기

'''
미로의 최단거리 경로(BFS)
7*7 격자판 미로를 탈출하는 최단 경로의 경로수를 출력하는 프로그램
출발점(1,1) , 도착점 (7,7) 격자판의 1은 벽, 0은 도로 움직임은 상하좌우로만 움직임
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
