import sys
from collections import deque

sys.stdin = open("0808/input0.txt", "rt")  # 파일 읽어오기

'''
재귀함수와 스택
'''


def DFS(x):
    if x > 0:
        # 위에 print하면 321
        DFS(x-1)
        print(x, end=' ')  # 재귀함수 밑에 하면 123 stack 때문임


if __name__ == "__main__":  # main임
    n = int(input())
    DFS(n)
