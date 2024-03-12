# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    res = 0
    for x in array:
        if max(array) < height:
            res = 0
            break
        if x > height:
            answer = x
            res += 1

    return res
