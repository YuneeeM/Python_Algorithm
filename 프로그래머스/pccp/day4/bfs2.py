# 미로탐험
h, w = map(int, input().split())
q = []
maze = []
visit = [[0 for i in range(w)] for i in range(h)]

for i in range(h):
    maze.append(input())


# 시작 위치 찾기
for k in range(h):
    for v in range(w):
        if maze[k][v] == '2':
            sh = k
            sw = v
            break

# q에 시작 값을 넣고 bfs 시작
q.append([sh, sw])
visit[sh][sw] = 1  # 나중에 -1해서 벽이랑 안 간곳 구분하기

while q:
    i, j = q.pop(0)

    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    # 범위, 방문, 방 인지?
    for k in range(4):
        nl = i + l[k]
        nc = j + c[k]
        if 0 <= nl < h and 0 <= nc < w:
            if visit[nl][nc] == 0:
                if maze[nl][nc] == '1':
                    visit[nl][nc] = visit[i][j] + 1
                    q.append([nl, nc])

for i in range(h):
    for j in range(w):
        if maze[i][j] == '0':  # 벽이면 0을 출력
            print(0, end=' ')
        else:
            # 모든 값에 -1을 해주면 방거리값과, 가지 못한 곳은 -1로 출력
            print(visit[i][j]-1, end=' ')
    print()
