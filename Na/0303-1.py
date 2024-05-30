# 숫자 카드 게임
n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_value = 10001
    for a in arr:
        min_value = min(a, min_value)

    result = max(result, min_value)

print(result)
