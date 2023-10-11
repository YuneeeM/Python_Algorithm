# 연속된 수의 합
num = 5
total = 5
arr = []

mid = total//num

i = mid+1
j = mid-1

while sum(arr) < total:

    if sum(arr)+i <= total:
        arr.append(i)
        i += 1
        print(arr)
    if sum(arr)+j <= total:
        arr.append(j)
        j -= 1
        print(j)
    if sum(arr) == total:
        break

arr.sort()
print(arr)
