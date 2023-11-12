# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for x in arr:
        if x != answer[-1]:
            answer.append(x)

    return answer
