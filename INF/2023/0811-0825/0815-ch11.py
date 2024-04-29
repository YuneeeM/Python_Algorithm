import sys
sys.stdin = open("0811/input11.txt", "rt")  # 파일 읽어오기
'''
등산경로(DFS)
n*n
어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 
더 높은 구역으로만 이동할 수 있음
출발지에서 도착지로 갈 수 있는 등산 경로가 몇가지 인지 구하기
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[x][y] < board[xx][yy]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    cnt = 0
    ch[sx][sy] = 1
    DFS(sx, sy)
    print(cnt)
