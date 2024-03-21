# 일곱 난쟁이 - 브루트포스/정렬

arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort()

sum_ = sum(arr)

# 만약 모두다 더하고 2명을 뺐을 때 그 값이 100이라면 2개를 뺀 나머지 값들 출력
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if sum_ - arr[i] - arr[j] == 100:
            for k in range(len(arr)):
                if k == i or k == j:
                    pass
                else:
                    print(arr[k])
            exit()
