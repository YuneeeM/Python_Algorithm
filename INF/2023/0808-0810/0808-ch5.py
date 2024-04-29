import sys
from collections import deque

sys.stdin = open("0808/input5.txt", "rt")  # 파일 읽어오기

'''
바둑이 승차(DFS)

철수는 그의 바둑이들을 데리고 시장에 가려고 함
그런데 그의 트럭은 c킬로그램 넘게 태울수가 없음
철수는 c를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶음
n마리의 바둑이와 각 바둑이의 무게 w가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운
무게를 구하는 프로그램

'''


def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
