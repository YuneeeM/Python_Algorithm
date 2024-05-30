# 큰 수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count)*first  # 가장 큰 수 더하기
result += (m-count)*second  # 두 번째로 큰수 더하기

print(result)  # 최종답안 출력
