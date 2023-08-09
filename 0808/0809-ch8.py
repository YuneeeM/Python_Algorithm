import sys
from collections import deque

sys.stdin = open("0808/input8.txt", "rt")  # 파일 읽어오기

'''
순열 구하기
1부터 n까지 번호가 적힌 구슬이 있음
이 중 m개를 뽑아 일렬로 나열하는 방법 모두를 출력
'''


def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    ch = [0]*(n+1)
    cnt = 0
    DFS(0)
    print(cnt)
