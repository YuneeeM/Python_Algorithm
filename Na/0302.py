# 큰 수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)  # 최종답안 출력
