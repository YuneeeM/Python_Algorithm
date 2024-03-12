# 가까운 수
def solution(array, n):
    answer = 0
    min_num = 101
    array.sort()
    for x in array:
        cur = abs(x-n)
        if min_num > cur:
            answer = x
            min_num = cur
    return answer
