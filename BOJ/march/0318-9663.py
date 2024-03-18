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

n = int(input())


def attack(x):  # 퀸이 공격을 받는지 확인
    for i in range(x):
        # 같은 행에 퀸이있거나 대각선에 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return True
        return False


def dfs(st):
    global count

    # 마지막까지 탐색했을 경우
    if st == n:
        count += 1
    else:
        for i in range(n):
            row[st] = i
            # 퀸의 위협을 받지 않는다면 다음 탐색
            if not attack(st):
                dfs(st+1)


# row[i]는 i행에 퀸이 있다는 의미
row = [0] * n
count = 0
dfs(0)

print(count)
