# 아파트 단지
w, h = map(int, input().split())

arr = []
visit = [[0 for i in range(w)] for j in range(h)]

maxn = 0
# n = 1

for i in range(h):
    arr.append(input())


def f(low, col):
    global n  # 전역변수 설정
    l = [0, 0, 1, -1]
    c = [1, -1, 0, 0]
    for i in range(4):
        # 범위 안에 있는가?
        nl = low+l[i]
        nc = col+c[i]
        if nl >= 0 and nl < h and nc >= 0 and nc < w:
            if visit[nl][nc] == 0 and arr[nl][nc] == "*":
                n += 1
                visit[nl][nc] = n  # 몇번째 섬인지를 체크
                f(nl, nc)


for i in range(h):
    for j in range(w):
        if visit[i][j] == 0 and arr[i][j] == "*":
            n = 1  # 방문처리(아파트 크기) 리셋 1부터
            visit[i][j] = n
            f(i, j)
            maxn = max(maxn, n)


print(maxn)
