# 가위 바위 보
def solution(rsp):
    answer = ''
    arr = [x for x in rsp]
    for x in range(len(arr)):
        if arr[x] == '2':
            answer += '0'
        elif arr[x] == '0':
            answer += '5'
        elif arr[x] == '5':
            answer += '2'
    return answer
