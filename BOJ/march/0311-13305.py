# 주유소 - 그리디
n = int(input())
km = list(map(int, input().split()))
oil = list(map(int, input().split()))

answer = 0
now = oil[0]

for i in range(n-1):
    if oil[i] < now:
        now = oil[i]
    answer += now * km[i]

print(answer)
