import sys
from collections import deque
sys.stdin = open("0826/input2.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)
'''
네트워크 선 자르기 (Top-Down : 재귀, 메모이제이션)
현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 함
'''


def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1)+DFS(len-2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))
