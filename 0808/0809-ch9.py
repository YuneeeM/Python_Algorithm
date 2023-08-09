import sys
from collections import deque

sys.stdin = open("0808/input9.txt", "rt")  # 파일 읽어오기


'''
수열 추측하기
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있음

3 1 2 4
 4 3 6
  7 9
  16
  
'''


def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0]*n
    b = [1]*n
    ch = [0]*(n+1)
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)
