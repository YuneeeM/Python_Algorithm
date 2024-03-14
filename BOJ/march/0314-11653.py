# 소인수분해 - 수학/정수론/소수 판정

n = int(input())

arr = []
i = 2
while n != 1:
    if n % i == 0:
        n = n / i
        arr.append(i)
    else:
        i = i+1

for a in arr:
    print(a)
