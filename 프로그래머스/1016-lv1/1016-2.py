# 3진법 뒤집기
def solution(n):
    answer = 0
    arr = []
    while n >= 3:
        arr.append(n % 3)
        n = n//3
    arr.append(n)

    for x in range(len(arr)):
        answer += arr.pop()*3**x

    return answer
