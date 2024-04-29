import sys
from collections import deque
sys.stdin = open("0811/input16.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)
'''
사다리 타기(DFS)

현수와 친구들은 과자를 사먹기 위해 사다리 타기를 함
사다리 표현은 2차원 평면은 0으로 채워지고, 사다리는 1로 표현함
현수는 특정도착지점으로 도착하기 위해서는 몇번째 열에서 출발해야 하는지 알고 싶음
특정 도착지점은 2로 표기됨

'''


def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)
