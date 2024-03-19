# 수 정렬하기 - 구현/정렬
n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

for i in arr:
    print(i)
