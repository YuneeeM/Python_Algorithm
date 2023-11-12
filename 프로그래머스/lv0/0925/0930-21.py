# 숫자 찾기
def solution(num, k):
    answer = 0
    arr = []
    n = len(str(num))
    for i in range(n-1, -1, -1):
        arr.append(num//10**i)
        num = num % 10**i
    for x in arr:
        if int(x) == k:
            answer = arr.index(x)+1
            break
        else:
            answer = -1
    return answer
