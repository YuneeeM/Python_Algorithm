import sys
from collections import deque
sys.stdin = open("0811/input14.txt", "rt")  # 파일 읽어오기

'''
안전영역(BFS)
어떤 지역의 높이 정보를 파악
그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇개가 만들어지는지 조사
장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)
