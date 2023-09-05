import sys
from collections import deque
sys.stdin = open("0826/input8.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
알리바바와 40인의 도둑(Top-Down)
알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망옴
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자함
각 돌다리들은 높이가 서로 다릅니다.
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다.
즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다. 
N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 
최소량을 구하는 프로그램을 작성하세요.

'''


def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return a[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y)+a[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1)+a[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1))+a[x][y]
        return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))
