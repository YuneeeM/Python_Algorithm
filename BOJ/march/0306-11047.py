# 동전 0 - 그리디 알고리즘
n, k = map(int, input().split())

coin = []
count = 0

for _ in range(n):
    i = int(input())
    coin.append(i)

coin.sort(reverse=True)

for c in coin:
    if c <= k:
        count += k // c
        k %= c

print(count)
