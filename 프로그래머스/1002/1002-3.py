# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    if n in array:
        answer = array.count(n)
        if answer > 0:
            return answer
    else:
        answer = 0
        return answer
