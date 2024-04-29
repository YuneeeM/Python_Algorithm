# 최소값 구하기[선수지식]

arr = [5, 3, 7, 9, 2, 5, 2, 6]

arrMin = float('inf')  # 가장 큰값이 초기화 됨
# arrMin =arr[0] 으로 처음 index값을 넣어도 된다.
for i in range(len(arr)):
    if (arrMin > arr[i]):  # 같다를 넣으면 순서를 신경쓰는 것 index의 뒷값을 고르겠다.
        arrMin = arr[i]
print(arrMin)
