import sys
from collections import deque

sys.stdin = open("0811/input1.txt", "rt")  # 파일 읽어오기

'''
최대 점수 구하기(DFS)
현수는 선생님이 주신 n개의 문제를 풀려고 함
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됨
m안에 n개의 문제 중 최대 점수를 얻을 수 있도록
'''


def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()  # 문제점수
    pt = list()  # 문제시간
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
