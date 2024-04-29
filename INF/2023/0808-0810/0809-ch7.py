import sys
from collections import deque

sys.stdin = open("0808/input7.txt", "rt")  # 파일 읽어오기

'''
동전교환
여러 단위의 동전들이 주어져 있을 때 거스름돈을 가장 적은 수의 동전으로 교환해주려면?

'''


def DFS(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)
