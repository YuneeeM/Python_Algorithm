import sys
from collections import deque

sys.stdin = open("0811/input2.txt", "rt")  # 파일 읽어오기

'''
휴가 (DFS 활용)
현수가 오늘부터 n+1일째 되는 날 휴가를 가기 위해서, 남은 n일 동안 최대한 많은 상담을 해서
휴가비를 넉넉히 만들어 휴가를 떠나려고 함
하루에 하나씩 서로 다른 사람의 상담이 예약됨
각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이루어짐
최대 수익을 구하는 프로그램
'''


def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+t[L] <= n+1:
            DFS(L+t[L], sum+p[L])  # 날짜에 잡힌 상담을 하는 것
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    t = list()  # 상담날수
    p = list()  # 상담금액
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    res = -2147000000
    t.insert(0, 0)
    p.insert(0, 0)
    DFS(1, 0)
    print(res)
