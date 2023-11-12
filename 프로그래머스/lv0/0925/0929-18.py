# 가장 큰 수 찾기
def solution(array):
    answer = []
    for x in array:
        if x == max(array):
            answer.append(x)
            answer.append(array.index(x))
    return answer
