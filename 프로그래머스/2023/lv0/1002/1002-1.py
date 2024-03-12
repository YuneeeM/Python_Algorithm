# 7의 개수
def solution(array):
    answer = 0
    array = [x for x in str(array)]
    for x in array:
        if x == "7":
            answer += 1
    return answer
