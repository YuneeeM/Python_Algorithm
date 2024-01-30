# 리코쳇 로봇

from collections import deque

l = [-1, 1, 0, 0]
c = [0, 0, 1, -1]


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    q = deque()
    dist = [[987654321 for _ in range(m)] for _ in range(n)]

    # 로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                dist[i][j] = 0
        if q:
            break

    while q:
        i, j, val = q.popleft()

        # 목표 지점(G)에 도착한 경우 이동 횟수 반환
        if board[i][j] == 'G':
            return val

        # 네 방향으로 이동할 수 있는 경우 탐색
        for k in range(4):
            nx = i
            ny = j

            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0 <= nx+l[k] < n and 0 <= ny+c[k] < m and board[nx+l[k]][ny+c[k]] != 'D':
                nx += l[k]
                ny += c[k]

            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[nx][ny] > val+1:
                dist[nx][ny] = val+1
                q.append((nx, ny, val+1))

    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1
