# 문자열 계산하기
def solution(my_string):
    arr = my_string.split()
    n = len(arr)
    answer = int(arr[0])

    for i in range(n):
        if arr[i] == '+':
            answer += int(arr[i+1])
        elif arr[i] == '-':
            answer -= int(arr[i+1])
        else:
            continue

    return answer
