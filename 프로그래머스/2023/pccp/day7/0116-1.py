# day 3 복습
# 1 - dfs (섬은 몇개일까) - 섬이 몇개인지

print("--------------------------------------------------")

w, h = map(int, input().split())

arr = []

visit = [[0 for i in range(w)] for i in range(h)]

for i in range(h):
    arr.append(list(map(int, input().split())))

n = 1


def f(low, col):
    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    for i in range(4):
        nl = low+l[i]
        nc = col+c[i]
        if 0 <= nl < h and 0 <= nc < w:
            if visit[nl][nc] == 0 and arr[nl][nc] == 1:
                visit[nl][nc] = n
                f(nl, nc)


for i in range(h):
    for j in range(w):
        if visit[i][j] == 0 and arr[i][j] == 1:
            visit[i][j] = n
            f(i, j)
            n += 1

print(n-1)


# 2 - dfs (아파트 단지) - 섬의 각각 개수 중 가장 큰거 찾기

print("--------------------------------------------------")

w, h = map(int, input().split())

arr = []

for i in range(h):
    arr.append(input())

visit = [[0 for i in range(w)] for i in range(h)]

maxn = 0


def f(low, col):
    global n
    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    for i in range(4):
        nl = low+l[i]
        nc = col+c[i]
        if 0 <= nl < h and 0 <= nc < w:
            if visit[nl][nc] == 0 and arr[nl][nc] == "*":
                n += 1
                visit[nl][nc] = n
                f(nl, nc)


for i in range(w):
    for j in range(h):
        if visit[i][j] == 0 and arr[i][j] == "*":
            n = 1
            visit[i][j] = n
            f(i, j)
            maxn = max(max, n)

# 3 - 재귀함수 (격자이동)

print("--------------------------------------------------")

ans = 0

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


def f(low, col, psum):
    global ans

    if low == n-1 and col == n-1:
        ans = max(ans, psum)

    if col+1 < n:
        f(low, col+1, psum+arr[low][col+1])
    if low+1 < n:
        f(low+1, col, psum+arr[low+1][col])


f(0, 0, arr[0][0])

print(ans)


# 4 - 재귀함수 (N부터 1까지 역순 출력)

print("--------------------------------------------------")


def num(N):
    if N == 0:
        return
    print(N)
    num(N-1)


n = int(input())
num(n)


# 5 - 재귀함수 (1부터 N까지 출력)

print("--------------------------------------------------")


def num(N):
    if N == 0:
        return
    f(N-1)
    print(N)


n = int(input())
num(n)


# 6 - 재귀함수 (1부터 N까지의 합)

print("--------------------------------------------------")


def num(N):
    if N == 1:
        return 1

    return N+num(N-1)


n = int(input())
print(num(n))


# 7 - 재귀함수 (바둑돌 배치하기)

print("--------------------------------------------------")

n, m = map(int, input().split())


def f(n, m):
    if n % 2 == 0 or m % 2 == 0:
        return 0

    return 1+4*f(n//2, m//2)


print(f(n, m))


# 8 - 재귀함수 ('O', 'X'의 모든경우의수만들기)

print("--------------------------------------------------")

n = int(input())


def f(cnt, st):
    if cnt == 0:
        print(st)
        return

    f(cnt-1, st+"O")
    f(cnt-1, st+"X")


f(n, "")


# 9 - 재귀함수 (숫자만들기)

print("--------------------------------------------------")

N, K = map(int, input().split())
Q = list(map(int, input().split()))


def f(maxnum, num):
    if N < maxnum:
        return maxnum

    maxnum = max(maxnum, num)
    for i in range(K):
        maxnum = f(maxnum, num*10 + Q[i])


print(f(0, 0))
