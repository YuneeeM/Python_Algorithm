# 소수 찾기 - 수학/정수론/소수 판정
n = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    for a in range(2, i+1):
        if i % a == 0:
            if i == a:
                cnt += 1

            break

print(cnt)
