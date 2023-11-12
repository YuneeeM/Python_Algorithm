# 중앙값 구하기
def solution(array):
    answer = 0
    array.sort()
    n = len(array)
    answer = array[n//2]
    return answer
