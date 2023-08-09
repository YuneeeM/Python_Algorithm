import sys
from collections import deque

sys.stdin = open("0808/input10.txt", "rt")  # 파일 읽어오기

'''
조합 구하기
1부터 N까지 번호가 적힌 구슬이 있음
이 중 M개를 뽑는 방법의 수 출력
'''


def DFS(L, sum):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(sum, n+1):
            res[L] = i
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*(n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
