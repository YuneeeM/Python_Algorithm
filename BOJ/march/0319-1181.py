# 단어 정렬 - 문자열/정렬
n = int(input())
arr = []
for _ in range(n):
    st = input()
    arr.append(st)

arr = list(set(arr))
arr.sort()

arr.sort(key=len)

for k in arr:
    print(k)
