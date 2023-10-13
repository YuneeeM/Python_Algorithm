# 제일 작은 수 제거하기
def solution(arr):
    answer = []
    if arr[0] == 10:
        answer.append(-1)
        return answer

    res = min(arr)
    arr.remove(res)

    answer = [x for x in arr]

    return answer
