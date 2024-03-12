# 격자이동
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


def max_grid_sum(n, arr):
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = arr[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + arr[i][0]
        dp[0][i] = dp[0][i-1] + arr[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1])

    return dp[n-1][n-1]


result = max_grid_sum(n, arr)
print(result)

print("---------------------------------")

ans = 0


def f(low, col, psum):
    # 전역변수 global
    global ans

    # 종료되는 조건 (끝 위치에 뒀다면)
    if low == n-1 and col == n-1:
        # 지금까지 가져온(합한) 값들 중에서 가장 큰 값을 찾아라(갱신)
        ans = max(ans, psum)

    # 가능할 때만 하겠다 (전제조건을 깔아줌) - 가능한 범위안에 있을 때만(!
    if col+1 < n:
        f(low, col+1, psum+arr[low][col+1])

    if low+1 < n:
        f(low+1, col, psum+arr[low+1][col])


# 현재 위치 low, col, psum
f(0, 0, arr[0][0])
