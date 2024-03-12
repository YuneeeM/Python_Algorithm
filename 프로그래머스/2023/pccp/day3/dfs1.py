# 섬은 몇개일까

# 가로, 세로
w, h = map(int, input().split())
# 지도
arr = []
for i in range(h):
    arr.append(list(map(int, input().split())))

# 방문 체크용 변수
visit = [[0 for i in range(w)]for j in range(h)]


def f(low, col):
    # 범위 안에 있는가?, 방문한적 없는가?, 섬인가?
    if col+1 < w and visit[low][col+1] == 0 and arr[low][col+1] == 1:
        visit[low][col+1] = n  # 몇번째 섬인지를 체크
        f(low, col+1)  # 오른쪽
    if col-1 >= 0 and visit[low][col-1] == 0 and arr[low][col-1] == 1:
        visit[low][col-1] = n
        f(low, col-1)  # 왼쪽
    if low+1 < h and visit[low+1][col] == 0 and arr[low+1][col] == 1:
        visit[low+1][col] = n
        f(low+1, col)  # 아래
    if low-1 >= 0 and visit[low-1][col] == 0 and arr[low-1][col] == 1:
        visit[low-1][col] = n
        f(low-1, col)  # 위


# 방문용도(섬 번호)
n = 1

# 모든 위치에서 재귀함수 실행
for i in range(h):
    for j in range(w):
        # 방문 한 적이 없으며 그리고, 섬이라면 재귀함수 실행
        if visit[i][j] == 0 and arr[i][j] == 1:
            visit[i][j] = n  # 섬의 번호
            f(i, j)  # 재귀함수 실행
            n += 1

print(n-1)

print("----------------------------------")

# 가장 큰 섬의 크기
# ans =0


def f(low, col):
    # global n
    l = [0, 0, 1, -1]
    c = [1, -1, 0, 0]
    for i in range(4):
        # 범위 안에 있는가?
        nl = low+l[i]
        nc = col+c[i]
        if nl >= 0 and nl < h and nc >= 0 and nc < w:
            if visit[nl][nc] == 0 and arr[nl][nc] == 1:
                # n+=1 -- 섬의 크기
                visit[nl][nc] = n  # 몇번째 섬인지를 체크
                f(nl, nc)


# 가로, 세로
w, h = map(int, input().split())
# 지도
arr = []
for i in range(h):
    arr.append(list(map(int, input().split())))
# 방문 체크용 변수
visit = [[0 for i in range(w)]for j in range(h)]

# 방문용도(섬 번호)
n = 1

# 모든 위치에서 재귀함수 실행
for i in range(h):
    for j in range(w):
        # 방문 한 적이 없으며 그리고, 섬이라면 재귀함수 실행
        if visit[i][j] == 0 and arr[i][j] == 1:
            # n=1 -- 섬의 크기 1 설정
            visit[i][j] = n  # 섬의 번호
            f(i, j)  # 재귀함수 실행
            # ans = max(ans,n) -- 가장 큰 섬의 크기 반환
            n += 1


print(n-1)
