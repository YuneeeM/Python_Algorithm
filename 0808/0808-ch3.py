import sys
from collections import deque

sys.stdin = open("0808/input3.txt", "rt")  # 파일 읽어오기

'''
부분집합 구하기(DFS)
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
'''


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end='')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)
