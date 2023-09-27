# 컨트롤 제트
def solution(s):
    answer = 0
    arr = s.split()
    n = len(arr)
    for i in range(n):
        if arr[i] == 'Z':
            answer -= int(arr[i-1])
        else:
            answer += int(arr[i])
    return answer
