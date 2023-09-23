# 배열 회전시키기
def solution(numbers, direction):

    n = len(numbers)
    arr = [0]*n

    if direction == "right":
        cur = numbers.pop()
        print(cur)
        for i in range(n):
            if i == 0:
                arr[i] = cur
                continue
            arr[i] = numbers[i-1]

    else:
        cur = numbers[0]
        for i in range(n):
            if i == n-1:
                arr[n-1] = cur
                break
            arr[i] = numbers[i+1]

    return arr
