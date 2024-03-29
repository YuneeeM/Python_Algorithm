# N-Queen - 브루트포스/백트래킹

'''
N*N 크기의 체스판 위에 퀸 N개 서로 공격할 수 없게 놓는 문제
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램

- 전형적인 백트래킹
- 모든 경우의 수를 살펴보는 브루트포스 기반
- 이후의 사건이 이전의 사건에 종속이므로 -> 가지치기
- 재귀를 통하여 백트래킹으로 품
- 같은 열, 대각선에 퀸이 존재하는 경우를 놓을 수 없음
'''

import sys
input = sys.stdin.readline


def attack(i):  # i행에 배치한 퀸 대해서 문제 없는지 확인
    for k in range(i):
        if row[i] == row[k] or abs(row[i] - row[k]) == abs(i - k):  # 같은 열이거나 같은 대각선
            return False
    return True


def backtracking(i):
    global result
    if i == N:  # 모든 행에 문제 없이 퀸을 배치했을 때
        result += 1
        return
    for j in range(N):
        if check[j]:  # 이미 퀸이 놓인 column
            continue
        row[i] = j  # i행 j열에 퀸 놓음
        if attack(i):
            check[j] = True  # j열 퀸 배치 체크
            backtracking(i + 1)  # 다음 행에 대해 수행
            check[j] = False  # j열 퀸 배치 해제


N = int(input())
row = [0] * N  # row[n] = m은 n행 m열에 퀸을 놓았음을 의미한다
check = [False] * N
result = 0

backtracking(0)

print(result)
