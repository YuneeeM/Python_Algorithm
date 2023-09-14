# 안전지대
def solution(board):
    n = len(board)

    ch = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ch.append((i, j))

    for x, y in ch:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny = y+dy
                nx = x+dx
                if 0 <= nx < n and 0 <= ny < n:
                    board[nx][ny] = 1
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                cnt += 1
    return cnt
